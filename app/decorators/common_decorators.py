#!/usr/bin/env python
# coding: utf-8
import functools
from flask import request, url_for, session, redirect
import hashlib
from flask_restful import abort
from flask import current_app
import json

from app import CommonResponse, ResultType


def paginate(max_per_page=100):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            page = request.args.get('page', 1, type=int)
            per_page = min(request.args.get('per_page', max_per_page,
                                            type=int),
                           max_per_page)

            query = func(*args, **kwargs)
            p = query.paginate(page, per_page)

            meta = {
                'page': page,
                'per_page': per_page,
                'total': p.total,
                'pages': p.pages,
            }

            links = {}
            if p.has_next:
                links['next'] = url_for(request.endpoint, page=p.next_num,
                                        per_page=per_page, **kwargs)
            if p.has_prev:
                links['prev'] = url_for(request.endpoint, page=p.prev_num,
                                        per_page=per_page, **kwargs)
            links['first'] = url_for(request.endpoint, page=1,
                                     per_page=per_page, **kwargs)
            links['last'] = url_for(request.endpoint, page=p.pages,
                                    per_page=per_page, **kwargs)

            meta['links'] = links
            result = {
                'items': p.items,
                'meta': meta
            }

            return result, 200

        return wrapped

    return decorator


def verify_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        x_timestamp = request.headers.get('X-TimeStamp')
        x_sign = request.headers.get('X-Sign')
        sign_key = current_app.config.get('SIGN_KEY')
        if not x_timestamp:
            abort(400, message=u"X-TimeStamp参数缺失")
        if not x_sign:
            abort(400, message=u"X-Sign参数缺失")

        data = request.get_data()
        sign = hashlib.new("md5", x_timestamp + data + sign_key).hexdigest().upper()
        if x_sign != sign:
            # 认证不通过
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def home_login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        current_user = session.get('current_user', None)
        if not current_user:
            if request.is_xhr:
                return CommonResponse(ResultType.Failed, message=u"请登录后，再继续操作").to_json()
            else:
                return redirect(url_for('home.login'))
        return func(*args, **kwargs)

    return wrapper
