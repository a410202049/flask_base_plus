#!/usr/bin/env python
# coding: utf-8
import functools
from flask import request, url_for, session, redirect
from app import CommonResponse, ResultType


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
