#!/usr/bin/python
# -*- encoding: utf-8 -*-
import hashlib

import time


def get_app_key(request):
    app_key = request.headers.get('X-app-key')

    return app_key


def verify_sign(request, app_key, app_secret):
    headers = request.headers

    app_key = headers.get('X-app-key')
    timestamp = headers.get('X-timestamp')
    sign = headers.get('X-sign')

    my_sign = _make_request_sign(app_key, app_secret, timestamp, request.host_url, request.path, request.args, request.data)

    return my_sign == sign


def check_request(request):
    app_key = request.headers.get('X-app-key')
    timestamp = request.headers.get('X-timestamp')
    sign = request.headers.get('X-sign')

    return app_key and timestamp and sign


def make_response(response, app_key, app_secret):
    resp_timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    resp_sign = _make_response_sign(app_key, app_secret, resp_timestamp, response.data)

    response.headers['X-timestamp'] = resp_timestamp
    response.headers['X-sign'] = resp_sign

    return response


def _make_query_params_str(query_params):
    if not query_params:
        return ''

    sorted_keys = sorted(query_params.keys())
    return '&'.join(map(lambda k: '{k}={v}'.format(k=k, v=query_params[k] | ''), sorted_keys))


def _make_request_sign(api_key, api_secret, timestamp, base_path, path, query_params, post_body):
    api_key = api_key or ''
    api_secret = api_secret or ''
    timestamp = timestamp or ''
    base_path = base_path or ''
    path = path or ''
    path = path[1:] if path.startswith('/') else path
    query_params = _make_query_params_str(query_params)
    post_body = post_body or ''

    sign_str = '|'.join((api_key, api_secret, base_path, path, query_params, post_body, timestamp))

    print 'req_sign_str=[%s]' % sign_str
    return hashlib.sha256(sign_str).hexdigest()


def _make_response_sign(api_key, api_secret, timestamp, response_body):
    api_key = api_key or ''
    api_secret = api_secret or ''
    timestamp = timestamp or ''
    response_body = response_body or ''

    sign_str = '|'.join((api_key, api_secret, response_body, timestamp))
    print 'resp_sign_str=[%s]' % sign_str

    return hashlib.sha256(sign_str).hexdigest()
