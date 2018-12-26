# -*- coding:utf-8 -*-
__author__ = u'kerry'

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    CONFIG_NAME = 'default'
    SECRET_KEY = '\x03d\xf4\x95J\x15\xa4B\xfb\xc0\xaf \xd1A[j$}\x18\x16a\xe7\xd0\xec'
    STRIPE_API_KEY = '\x03d\xf4\x95J\x15\xa4B\xfb\xc0\xaf \xd1A[j$}\x18\x16a\xe7\xd0\xec'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    WTF_CSRF_ENABLED = False
    PAGE_SIZE = 15
    SQLALCHEMY_ECHO = False

    NETWORK_FORMATTER = '[%(levelname)1.1s][%(method)s][tm:%(asctime)s][request_id:%(request_id)s]' \
                        '[file:%(module)s:%(funcName)s:%(lineno)d] %(message)s'

    LOG_PATH = 'src.log'

    VERSION = '1.0.1'
    IS_LOCALHOST = True

    # 邮件配置
    MAIL_SERVER = 'smtp.xxxx.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'xxx@xxx.com'
    MAIL_PASSWORD = '11111111'

    # REDIS CONFIG
    REDIS_CACHES = {
        'host': '127.0.0.1',
        'port': '6379',
        'db': 0,
        'password': ''
    }

    # 所有SQLALCHEMY配置项可参考手册http://www.pythondoc.com/flask-sqlalchemy/config.html#id2
    @staticmethod
    def init_app(app):
        pass


class LocalConfig(Config):
    CONFIG_NAME = 'local'
    SQLALCHEMY_DATABASE_URI = "mysql://root:Kerrygao123@47.74.251.5/flask_base_plus?charset=utf8"


class DevelopmentConfig(Config):
    CONFIG_NAME = 'devel'
    SQLALCHEMY_DATABASE_URI = "mysql://xxxxx:xxxx@xxxxxxxxxxxxxxxxxx/cqgcu_enroll?charset=utf8"


class ProductionConfig(Config):
    CONFIG_NAME = 'product'
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/cqgcu?charset=utf8"


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'local': LocalConfig,
}
