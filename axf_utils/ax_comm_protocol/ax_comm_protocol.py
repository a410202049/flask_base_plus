#!/usr/bin/python
# -*- encoding: utf-8 -*-
import abc
import hashlib
import json
import sys
import urllib
import urlparse
import base64
import time
import requests
import six
from requests import ConnectionError, RequestException

from axf_utils.dict_util import to_pretty_json_string
from .. import to_str, to_unicode
from ..ax_comm_protocol import IllegalResponseException, FailResponseException, AP_ILLEGAL_SIGNATURE, \
    IllegalRequestException, IllegalResponseSignatureException, ConnectionFailedError, AP_BASE_RESP_NOT_FOUND, \
    AP_RESP_CODE_NOT_FOUND, AP_HTTP_STATUS_CODE_ERROR, AP_INVALID_REQUEST, verify_http_status_code, \
    IllegalResponseHeadersException
from ..context.api_context import ApiContext
from ..context.app_context import AppContext
from ..exception import AxBaseException
from ..structed_log.api_log import ApiLog
from ..structed_log.app_log import AppLog
from ..structed_log.network_log import NetworkOutLog


def _create_sign(request_text, key):
    request_text = to_str(request_text)
    key = to_str(key)

    sign_text = request_text + key
    m = hashlib.md5()
    m.update(sign_text)
    return m.hexdigest()


class AxRequestHandler(object):
    def __init__(self,
                 sign_key=None,
                 json_name='json',
                 sign_name='sign',
                 success_code=0,
                 base_req_name='req',
                 base_resp_name='resp',
                 resp_code_name='resp_code',
                 resp_msg_name='resp_desc',
                 protocol_name='ax_comm_protocol',
                 protocol_version='v1.0'):

        self.sign_key = sign_key
        self.json_name = json_name
        self.sign_name = sign_name
        self.success_code = success_code
        self.base_req_name = base_req_name
        self.base_resp_name = base_resp_name
        self.resp_code_name = resp_code_name
        self.resp_msg_name = resp_msg_name
        self.protocol_name = protocol_name
        self.protocol_version = protocol_version

    def create_sign(self, key, service, method, request_text):
        return _create_sign(request_text, key)

    def handle_http_request(self, context, service, method, args=None, from_ip=None):
        if isinstance(context, AppContext):
            app_context = context
        else:
            app_context = AppContext(context, self.protocol_name, self.protocol_version, service, method, from_ip)
        log = AppLog(app_context)

        log.i('got request %s' % to_pretty_json_string(
            ip=from_ip,
            service=service,
            method=method,
            args=args
        ))

        try:
            if not service or not method:
                log.i('invalid request, service or method not found')
                raise IllegalRequestException(u'无效请求')

            if self.json_name not in args:
                log.i('%s or %s not found in request' % (self.json_name, self.sign_name))
                raise IllegalRequestException(u'无效请求')

            if self.sign_key and self.json_name not in args:
                log.i('%s or %s not found in request' % (self.json_name, self.sign_name))
                raise IllegalRequestException(u'无效请求')

            json_text = args[self.json_name]

            if self.sign_key:
                sign = args.get(self.sign_name, None)
                my_sign = self.create_sign(self.sign_key, service, method, json_text)

                if sign != my_sign:
                    log.i('signature=[%s] is not equals my signature=[%s]' % (sign, my_sign))
                    raise IllegalRequestException(u'未能通过签名验证', AP_ILLEGAL_SIGNATURE)

            request_dict = json.loads(json_text)

            if not isinstance(request_dict, dict):
                app_context.log.w('request data is not json object but string: %s' % request_dict)
                raise IllegalRequestException(u'请示参数不正确', AP_INVALID_REQUEST)

            response_dict = self.handle_request(app_context, service, method, request_dict)
            log.d('response: %s' % to_pretty_json_string(**response_dict))
            response = self.create_response(app_context, self.success_code, 'success', response_dict)
        except AxBaseException, ex:
            response = self.create_response(app_context, ex.error_code, ex.error_msg, ex.error_data)
            log.e('error: %s' % to_pretty_json_string(
                message=ex.message,
                error_message=ex.error_msg,
                error_code=ex.error_code
            ))

        return response

    def handle_request(self, app_context, service_name, method_name, req):
        raise NotImplementedError('handle_request not implemented')

    def create_response(self, app_context, resp_code, resp_msg, resp_dict):
        response = {
            self.base_resp_name: {self.resp_code_name: resp_code, self.resp_msg_name: resp_msg},
        }

        if resp_dict:
            response.update(resp_dict)

        json_text = json.dumps(response)

        response_map = {self.json_name: json_text}
        if self.sign_key:
            sign = _create_sign(json_text, self.sign_key)
            response_map[self.sign_name] = sign

        return urllib.urlencode(response_map)


class AxRequestAgent(object):
    def __init__(self, base_url,
                 sign_key=None,
                 json_name='json',
                 sign_name='sign',
                 success_code=0,
                 base_req_name='req',
                 base_resp_name='resp',
                 resp_code_name='resp_code',
                 resp_msg_name='resp_desc',
                 protocol_name='ax_comm_protocol',
                 protocol_version='v1.0',
                 ignore_ssl_verify_error=True):

        self.base_url = base_url

        self.sign_key = sign_key
        self.json_name = json_name
        self.sign_name = sign_name
        self.success_code = success_code
        self.base_req_name = base_req_name
        self.base_resp_name = base_resp_name
        self.resp_code_name = resp_code_name
        self.resp_msg_name = resp_msg_name
        self.protocol_name = protocol_name
        self.protocol_version = protocol_version
        self.verify_ssl_cert = not ignore_ssl_verify_error

    def create_sign(self, key, service, method, request_text):
        return _create_sign(request_text, key)

    def create_base_request(self, api_context):
        return None

    def create_request_url(self, api_context, base_url):
        return base_url

    def create_api_context(self, context, service, method, customer_no):
        return ApiContext(context, self.protocol_name, self.protocol_version, service, method, customer_no)

    def do_request(self, context, service, method, customer_no, req_data):
        if isinstance(context, ApiContext):
            api_context = context
        else:
            api_context = ApiContext(context, self.protocol_name, self.protocol_version, service, method, customer_no)

        url = self.create_request_url(api_context, self.base_url)
        base_req = self.create_base_request(api_context)

        log = ApiLog(api_context)

        log.i('start request: %s' % to_pretty_json_string(
            service=service,
            method=method,
            url=url,
            request=req_data
        ))

        req_data[self.base_req_name] = base_req

        json_text = json.dumps(req_data)

        request = {self.json_name: json_text}

        if self.sign_key:
            sign_text = self.create_sign(self.sign_key, service, method, json_text) if self.sign_key else None
            log.d('do_request got signature=[%s]' % sign_text)
            request[self.sign_name] = sign_text

        try:
            parse_resp = self.do_http_request(context, url, request)
        except ConnectionError, e:
            log.w('%s.%s end request=[%s] to url=[%s] with error=[%s]' % (service, method, req_data, url, e))
            raise ConnectionFailedError(u'系统暂时不可用, 请稍后再试'), None, sys.exc_info()[2]

        if self.json_name not in parse_resp:
            log.w('%s.%s end request=[%s] to url=[%s] with error=[%s]' %
                  (service, method, req_data, url, 'json or signature not found in response'))
            raise IllegalResponseException(u'系统暂时不可用, 请稍后再试')

        if self.sign_key and self.sign_name not in parse_resp:
            log.w('%s.%s end request=[%s] to url=[%s] with error=[%s]' %
                  (service, method, req_data, url, 'json or signature not found in response'))
            raise IllegalResponseException(u'系统暂时不可用, 请稍后再试')

        json_text = parse_resp[self.json_name]
        sign = parse_resp.get(self.sign_name, None)

        if self.sign_key:
            log.i(u'sign source: {0}'.format(json_text))
            my_sign = _create_sign(json_text, self.sign_key)

            if my_sign != sign:
                log.d('do_request response sign={0}, my_sign={1}'.format(sign, my_sign))
                raise IllegalResponseSignatureException(u'系统暂时不可用, 请稍后再试')

        response = json.loads(json_text)

        response = response if response is not None else {}

        resp_code, resp_msg, response = self.parse_response(response)

        if resp_code != self.success_code:
            if self.base_resp_name:
                response.pop(self.base_resp_name)
            raise FailResponseException(resp_msg, resp_code, response)

        return response

    def parse_response(self, response):
        if self.base_resp_name:
            if self.base_resp_name not in response:
                raise IllegalResponseException(u'系统暂时不可用, 请稍后再试', AP_BASE_RESP_NOT_FOUND)

            resp = response[self.base_resp_name]
        else:
            resp = response

        if self.resp_code_name not in resp:
            raise IllegalResponseException(u'系统暂时不可用, 请稍后再试', AP_RESP_CODE_NOT_FOUND)

        resp_code = resp[self.resp_code_name]
        resp_msg = resp.get(self.resp_msg_name, None)

        return resp_code, resp_msg, response

    def do_http_request(self, context, url, params):
        log = NetworkOutLog(context, 'POST', url)
        log.i('do request to: %s' % to_pretty_json_string(
            url=url,
            params=params
        ))

        try:
            response = requests.post(url, params, verify=self.verify_ssl_cert)
        except RequestException, ex:
            log.w('end http request url=[%s] request=[%s] error=[%s]' % (url, params, ex))
            raise

        log.i('do request to: %s' % to_pretty_json_string(
            url=url,
            params=params
        ))

        verify_http_status_code(response.status_code, u'系统暂时不可用, 请稍后再试')

        resp_text = response.content
        parse_resp = dict(urlparse.parse_qsl(resp_text))

        return parse_resp


class BasicAuthRequestAgent(object):
    """
    使用 Basic Authrization 校验的请求agent
    """
    def __init__(self, base_url, username, password, base_req_name='req',
                 base_resp_name='resp', sign_name=None, sign_key=None,
                 ignore_ssl_verify_error=True, resp_code_name='respCode',
                 resp_msg_name='respDesc', success_code='SD0000'):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.base_req_name = base_req_name
        self.base_resp_name = base_resp_name
        self.sign_name = sign_name
        self.sign_key = sign_key
        self.verify_ssl_cert = ignore_ssl_verify_error
        self.resp_code_name = resp_code_name
        self.resp_msg_name = resp_msg_name
        self.success_code = success_code

    def create_base_request(self, api_context):
        raise NotImplementedError

    @staticmethod
    def create_sign(key, service, method, request_text):
        return _create_sign(request_text, key)

    def do_request(self, context, api_name, method, customer_no, req_data):
        if isinstance(context, ApiContext):
            api_context = context
        else:
            api_context = ApiContext(context, service=api_name, method=method, customer_no=customer_no)

        base_req = self.create_base_request(api_context)

        log = ApiLog(api_context)

        log.i('start request: %s' % to_pretty_json_string(
            url=self.base_url,
            api_name=api_name,
            method=method,
            req_data=req_data
        ))

        req_data[self.base_req_name] = base_req

        json_text = json.dumps(req_data)

        if self.sign_key and self.sign_name:
            sign_text = self.create_sign(self.sign_key, api_name, method, json_text) if self.sign_key else None
            log.d('signature=[%s]' % sign_text)
            req_data[self.sign_name] = sign_text
        req_url = '/'.join([self.base_url, api_name, method])
        try:
            parse_resp = self.do_http_request(context, req_url, req_data)
        except ConnectionError, e:
            log.w('%s.%s end request=[%s] to url=[%s] with error=[%s]' % (api_name, method, req_data, req_url, e))
            raise ConnectionFailedError(u'系统暂时不可用, 请稍后再试'), None, sys.exc_info()[2]

        if (self.resp_code_name not in parse_resp.keys()) or (self.resp_msg_name not in parse_resp.keys()):
            log.w('%s.%s end request=[%s] to url=[%s] with error=[%s]' %
                  (api_name, method, req_data, req_url, 'resp_code or resp_msg not found in response'))
            raise IllegalResponseException(u'系统暂时不可用, 请稍后再试')

        log.d('%s.%s got result=%s' % (api_name, method, parse_resp))

        if parse_resp[self.resp_code_name] != self.success_code:
            resp_code = parse_resp[self.resp_msg_name]
            resp_msg = parse_resp[self.resp_code_name]
            if self.resp_code_name:
                parse_resp.pop(self.resp_code_name)

            if self.resp_msg_name:
                parse_resp.pop(self.resp_msg_name)
            log.w('%s.%s end request=[%s] to url=[%s] with error=[%s]' %
                  (api_name, method, req_data, req_url, (resp_code, resp_msg, parse_resp)))
            raise FailResponseException(resp_code, resp_msg, parse_resp)

        log.i('%s.%s end request=[%s] to url=[%s] with response=[%s]' %
              (api_name, method, req_data, req_url, parse_resp))

        return parse_resp

    def do_http_request(self, context, url, params):
        log = NetworkOutLog(context, 'POST', url)
        log.i('start http request url=[%s] params=[%s]' % (url, params))
        try:
            headers = {'content-type': 'application/json;charset=utf-8',
                       'Authorization': ' '.join(['Basic', base64.b64encode(':'.join([self.username, self.password]))])}
            response = requests.post(url, data=json.dumps(params), verify=self.verify_ssl_cert, headers=headers)
        except RequestException, ex:
            log.w('end http request url=[%s] request=[%s] error=[%s]' % (url, params, ex))
            raise

        log.i('end http request url=[%s] request=[%s] status_code=[%s] response=[%s]' %
              (url, params, response.status_code, to_unicode(response.content)))

        verify_http_status_code(response.status_code, u'系统暂时不可用, 请稍后再试')

        resp_text = response.content
        parse_resp = dict(urlparse.parse_qsl(resp_text))

        return json.loads(resp_text, parse_float=str)

    def parse_response(self, response):
        pass


@six.add_metaclass(abc.ABCMeta)
class BaseRequestAgent(object):
    """
    请求代理
    """
    @abc.abstractmethod
    def build_req_header(self):
        """
        构建header
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def parse_resp_body(self, response):
        """
        解析response
        :return: 
        """
        raise NotImplementedError

    @abc.abstractmethod
    def parse_resp_header(self):
        """
        解析 header
        :return:
        """
        raise NotImplementedError

    @staticmethod
    def verify_http_status_code(status_code, fail_message=u'系统暂时不可用, 请稍后再试'):
        if 400 <= status_code < 600:
            raise ConnectionFailedError(fail_message, 'SA1%03d' % status_code)


class AxfRestfulRequestAgent(BaseRequestAgent):
    def __init__(self, base_url, sign_key, auth_code=None):
        """
        构建 agent
        :param base_url: 
        :param sign_key: 
        :param auth_code:
        response:
        {
        "resp": {
            "biz_code": "string",
            "biz_desc": "string",
            "resp_code": "string",
            "resp_desc": "string"
          },
        "data": ""
        }
        """
        self.url = base_url
        self._sign_key = sign_key
        self._timestamp = str(time.time()).replace('.', '')
        self._content_type = 'application/json; charset=utf-8'
        self._base_resp_name = 'resp'
        self._resp_code_name = 'resp_code'
        self._resp_desc_name = 'resp_desc'
        self._biz_code_name = 'biz_code'
        self._biz_desc_name = 'biz_desc'
        self._resp_success_code = '00'
        self._biz_success_code = '00'
        self._auth_code = auth_code
        super(AxfRestfulRequestAgent, self).__init__()

    def build_req_header(self, sign):
        """
        生成请求header
        :return:
        :param sign:
        :return: 
        """
        header = {
            'content-type': self._content_type,
            'X-api-sign': sign,
            'X-api-timestamp': self._timestamp,
        }

        if self._auth_code:
            header.update({'X-user-id': self._auth_code})

        return header

    def parse_resp_body(self, response):
        resp_dict = json.loads(response)

        if self._base_resp_name not in resp_dict.keys():
            raise IllegalResponseHeadersException(u'系统暂时不可用, 请稍后再试')

        base_resp = resp_dict.get(self._base_resp_name, None)
        if (self._resp_code_name not in base_resp.keys()) \
                or (self._resp_code_name not in base_resp.keys()) \
                or (self._biz_code_name not in base_resp.keys()) \
                or (self._biz_desc_name not in base_resp.keys()):
            raise IllegalResponseHeadersException(u'系统暂时不可用, 请稍后再试')

        if base_resp.get(self._resp_code_name) != self._resp_success_code:
            code = base_resp.get(self._resp_code_name)
            code = '0000' if code == '00' else '9999'
            raise IllegalResponseException(base_resp.get(self._resp_desc_name),
                                           ''.join(['AQR', code]))

        if base_resp.get(self._biz_code_name) != self._biz_success_code:
            code = base_resp.get(self._biz_code_name)
            code = '0000' if code == '00' else '9999'
            raise IllegalResponseException(base_resp.get(self._biz_desc_name),
                                           ''.join(['AQR', code]))
        resp_dict.pop(self._base_resp_name)
        return resp_dict

    @staticmethod
    def create_sign(sign_key, request_text):
        return _create_sign(request_text, sign_key)

    @staticmethod
    def parse_resp_header(resp_headers):
        """
        解析响应头
        :param resp_headers: 
        :return: 
        """
        if resp_headers is None:
            raise IllegalResponseHeadersException(u'系统暂时不可用, 请稍后再试')

        if 'X-signature' not in resp_headers.keys():
            raise IllegalResponseHeadersException(u'系统暂时不可用, 请稍后再试')

        return resp_headers.get('X-signature')

    def get(self, context, uri, params):
        url = '/'.join([self.url, uri])
        log = NetworkOutLog(context, 'GET', url)

        headers = self.build_req_header(
            self.create_sign(self._sign_key, ''.join([self._timestamp])))
        log.i('do request to: %s' % to_pretty_json_string(
            url=url,
            params=params
        ))
        try:
            response = requests.get(url, params, headers=headers)
        except RequestException, ex:
            log.w('end http request url=[%s] request=[%s] error=[%s]' % (self.url + uri, params, ex))
            raise

        log.i('got response: %s' % to_pretty_json_string(
            status_code=response.content,
            parms=to_unicode(response.content)
        ))

        if response.status_code != 200:
            raise IllegalResponseException(u'请求异常, 请稍后再试', AP_HTTP_STATUS_CODE_ERROR)

        self.parse_resp_body(response.text)

        return json.loads(response.text)

    def post(self, context, uri, params):
        url = '/'.join([self.url, uri])
        log = NetworkOutLog(context, 'POST', url)
        try:
            headers = self.build_req_header(
                self.create_sign(self._sign_key, ''.join([json.dumps(params) if params else '', self._timestamp])))
            log.i('start http request url=[%s] params=[%s] headers=[%s]'
                  % (url, json.dumps(params), json.dumps(headers)))
            response = requests.post(url + '/', json=params,
                                     headers=headers)
        except RequestException, ex:
            log.w('end http request url=[%s] request=[%s] error=[%s]' % (url, params, ex))
            raise

        log.i('end http request url=[%s] request=[%s] status_code=[%s] response=[%s]' %
              (url, params, response.status_code, to_unicode(response.content)))

        self.verify_http_status_code(response.status_code)
        self.parse_resp_body(response.content)

        result = json.loads(response.content)

        # my_resp_sign = self.create_sign(self._app_secret, json.dumps(result))
        # resp_sign = self.parse_resp_headers(response.headers)
        # log.i('resp sign=[{0}] and my_sign=[{1}]'.format(resp_sign, my_resp_sign))
        # if my_resp_sign != resp_sign:
        #     raise IllegalResponseHeadersException(u'系统暂时不可用, 请稍后再试')

        return result


class RealNameValidRequestAgent(object):
    def __init__(self, base_url, app_code):
        self.url = base_url
        self.app_code = app_code
        super(RealNameValidRequestAgent, self).__init__()

    def parse_response(self, response):
        response = response[response.find('{'):]
        resp_dict = json.loads(response)

        if ('error_code' not in resp_dict.keys()) and ('result' not in resp_dict.keys()):
            raise IllegalResponseException(u'身份认证系统错误', resp_dict['error_code'])

        return resp_dict['result']

    def get(self, context, uri, params):
        log = NetworkOutLog(context, 'GET', self.url + uri)

        log.i('do request to: %s' % to_pretty_json_string(
            url=self.url,
            params=params
        ))
        try:
            headers = {'content-type': 'application/json;charset=utf-8',
                       'Authorization': ' '.join(['APPCODE', self.app_code])}
            response = requests.get(self.url + uri, params, headers=headers)
        except RequestException, ex:
            log.w('end http request url=[%s] request=[%s] error=[%s]' % (self.url + uri, params, ex))
            raise

        log.i('got response: %s' % to_pretty_json_string(
            status_code=response.content,
            parms=to_unicode(response.content)
        ))

        if response.status_code != 200:
            raise IllegalResponseException(u'实名认证请求异常, 请稍后再试', AP_HTTP_STATUS_CODE_ERROR)

        resp_text = response.text

        parse_resp = self.parse_response(resp_text)

        return parse_resp
