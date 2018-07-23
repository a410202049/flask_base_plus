#!/usr/bin/python
# -*- encoding: utf-8 -*-
from ..exception import AxBaseException

# general
AP_GENERAL_ERROR = 'SA0000'
AP_INVALID_RESPONSE = 'SA0001'
AP_FAILED_RESPONSE = 'SA0002'
AP_INVALID_REQUEST = 'SA0003'
AP_ILLEGAL_SIGNATURE = 'SA0004'
AP_CONNECTION_ERROR = 'SA0005'
AP_BASE_RESP_NOT_FOUND = 'SA0006'
AP_RESP_CODE_NOT_FOUND = 'SA0007'
AP_INVALID_RESP_SIGN = 'SA0009'
AP_INVALID_RESP_HEADERS = 'SA0010'


AP_HTTP_STATUS_CODE_ERROR = 'SA1000'
AP_HTTP_STATUS_CODE_ERROR400 = 'SA0400'
AP_HTTP_STATUS_CODE_ERROR404 = 'SA0404'
AP_HTTP_STATUS_CODE_ERROR401 = 'SA0010'


def verify_http_status_code(status_code, fail_message=u'系统暂时不可用, 请稍后再试'):
    if 400 <= status_code < 600:
        raise ConnectionFailedError(fail_message, 'SA1%03d' % status_code)


class ConnectionFailedError(AxBaseException):
    def __init__(self, message, error_code=AP_CONNECTION_ERROR):
        super(ConnectionFailedError, self).__init__(message, error_code)


class IllegalResponseException(AxBaseException):
    def __init__(self, message, error_code=AP_INVALID_RESPONSE):
        super(IllegalResponseException, self).__init__(message, error_code)


class IllegalResponseSignatureException(AxBaseException):
    def __init__(self, message):
        super(IllegalResponseSignatureException, self).__init__(message, AP_INVALID_RESP_SIGN)


class IllegalResponseHeadersException(AxBaseException):
    def __init__(self, message):
        super(IllegalResponseHeadersException, self).__init__(message, AP_INVALID_RESP_HEADERS)


class IllegalRequestException(AxBaseException):
    def __init__(self, error_msg=u'无效的请求数据', error_code=AP_INVALID_REQUEST):
        super(IllegalRequestException, self).__init__(error_msg, error_code)


class FailResponseException(AxBaseException):
    def __init__(self, error_msg=None, error_code=AP_FAILED_RESPONSE, resp_data=None):
        super(FailResponseException, self).__init__(error_msg, error_code, resp_data)
