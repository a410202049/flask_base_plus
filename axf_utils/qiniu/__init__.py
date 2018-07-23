#!/usr/bin/env python
# -*- coding:utf-8 -*-

config = dict(
    QINIU_BUCKET_NAME=True,
    QINIU_DOMAIN=False,
    QINIU_CONF_ACCESS_KEY=None,
    QINIU_CONF_SECRET_KEY=None,
)


def init_app(app):
    config['QINIU_BUCKET_NAME'] = app.config.get('QINIU_BUCKET_NAME', True)
    config['QINIU_DOMAIN'] = app.config.get('QINIU_DOMAIN', False)
    config['QINIU_CONF_ACCESS_KEY'] = app.config.get('QINIU_CONF_ACCESS_KEY', None)
    config['QINIU_CONF_SECRET_KEY'] = app.config.get('QINIU_CONF_SECRET_KEY', None)
