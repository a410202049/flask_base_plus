# coding: utf-8
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy, get_debug_queries, BaseQuery
from flask_login import LoginManager

from app.exception.exception import ServerBaseException
from app.utils.context.context import Context
from app.utils.restful_response import CommonResponse, ResultType
from config import config
from werkzeug.utils import import_string

import time
from utils import context
from utils.logger.log import init_logger_from_object
from utils.logger import log as logging

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

logger = logging.get_logger()
# 设置db.session.query 可以使用分页类
session_options = {}
session_options['query_cls'] = BaseQuery
session_options['autocommit'] = False
session_options['autoflush'] = False
session_options['expire_on_commit'] = False

db = SQLAlchemy(session_options=session_options)

login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'admin.login'
login_manager.login_message = None
VERSION = '1.0.0'


# jinja2 None to ''
def finalize(arg):
    if arg is None:
        return ''
    return arg


def register_blueprints(app):
    # 注册蓝图
    blueprints = [
        "app.controller.admin:admin",
        "app.controller.home:home"
    ]
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)


class DBSessionForRead(object):

    def __enter__(self):
        self.session = db.create_scoped_session(options=session_options)
        # self.session = db.session
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        # db.session.expunge_all()
        self.session.close()


class DBSessionForWrite(object):

    def __enter__(self):
        self.session = db.create_scoped_session(options=session_options)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

        # db.session.expunge_all()
        self.session.close()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    app.config['MAX_CONTENT_LENGTH'] = app.config.get('MAX_CONTENT_LENGTH')

    init_logger_from_object(config[config_name])

    # 开启调试模式
    app.debug = app.config.get('DEBUG')

    # jinja2 None to ''
    app.jinja_env.finalize = finalize

    # init utils
    import utils
    utils.init_app(app)

    # context init
    context.init_app(app)

    # # init db
    # from utils import db_session
    # db_session.init_app(app)

    # init redis
    from utils import redis_cache
    redis_cache.init_app(app)

    from app import template_filter
    template_filter.init_app(app)

    # 初始化路由
    import routing
    routing.init_routing(app)

    # 注册蓝图
    register_blueprints(app)

    # 添加当前时间戳 全局变量
    app.add_template_global(int(time.time()), 'current_time')

    @app.after_request
    def after_request(response):
        for query in get_debug_queries():
            if query.duration >= current_app.config['FLASKY_SLOW_DB_QUERY_TIME']:
                current_app.logger.warning(
                    'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                    % (query.statement, query.parameters, query.duration,
                       query.context))
        return response

    @app.errorhandler(Exception)
    def handle_exception(e):
        if current_app.config['CONFIG_NAME'] != 'local':
            if not isinstance(e, ServerBaseException):
                logger.exception(u'service has exception: {0}'.format(e.message))
                import traceback
                from utils import email_util
                title = u'Server-%s-%s' % (current_app.config['CONFIG_NAME'], email_util.get_exception_message(e))
                body = u'Server异常: \n{message}'.format(message=traceback.format_exc())
                email_util.send_warning_email(title, body, ['gaoyuan@axinfu.com'])
        return e.message

    return app


