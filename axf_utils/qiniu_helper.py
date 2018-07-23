#!/usr/bin/env python
# -*- coding:utf-8 -*-


import qiniu.conf
import qiniu.rs

bucket_name = 'zhax-xiaozhang'
domain = '7ls0zg.com1.z0.glb.clouddn.com'
qiniu.conf.ACCESS_KEY = 'd7Og6iYcRPguk6RGooiwBccSFxu1x3tme6ZxwcZZ'
qiniu.conf.SECRET_KEY = '_FVaqVvvGB2MH_xxAqj78MRZ8UuQMMjFpJ2X7bsx'


def upload_token(file_name, callback_url=None):
    scope = '%s:%s' % (bucket_name, file_name)
    policy = qiniu.rs.PutPolicy(scope)
    if callback_url is not None:
        policy.callbackUrl = callback_url
        policy.callbackBody = "bucket=$(bucket)&key=$(key)"
    uptoken = policy.token()

    return uptoken


def download_url(key, is_private=False):
    base_url = qiniu.rs.make_base_url(domain, key)

    if is_private:
        policy = qiniu.rs.GetPolicy()
        private_url = policy.make_request(base_url)

        return private_url
    else:
        return base_url
