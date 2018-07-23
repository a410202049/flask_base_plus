#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
from axf_utils.mem_cache.enum_redis import EnumRedis

config = dict(
    DEBUG=True,
    LOCAL=False,
    REDIS_CACHES=None,
)

client = None


def init_app(app):

    config['DEBUG'] = app.config.get('DEBUG', True)
    config['LOCAL'] = app.config.get('LOCAL', False)
    config['REDIS_CACHES'] = app.config.get('REDIS_CACHES', None)
    connection_pool = redis.ConnectionPool(**config['REDIS_CACHES'])

    if config['DEBUG'] and config['LOCAL']:
        client = EnumRedis()
    else:
        global client
        client = redis.Redis(connection_pool=connection_pool)


def get_client():
    return client
