# coding: utf-8
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy, get_debug_queries, BaseQuery
from flask_login import LoginManager

from app.utils.restful_response import CommonResponse, ResultType
from config import config
from werkzeug.utils import import_string

import time
from app.utils.log import FinalLogger

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# mail = Mail()

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
        "app.controller.admin:admin"
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
    # 开启调试模式
    app.debug = app.config.get('DEBUG')

    # jinja2 None to ''
    app.jinja_env.finalize = finalize

    # 配置log路径
    log_handler = FinalLogger(app).getLogger()
    app.logger.addHandler(log_handler)

    # import axf_utils
    # axf_utils.init_app(app)

    from app import template_filter
    template_filter.init_app(app)

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

    @app.teardown_appcontext
    def shutdown_session(exception):
        # current_app.logger.warning(exception)
        db.session.remove()

    # @app.errorhandler(Exception)
    # def handle_exception(ex):
    #     if current_app.config['CONFIG_NAME'] != 'local':
    #         if not isinstance(ex, AxBaseException):
    #             context = Context()
    #             context.log.e('notify handle error: {0}'.format(ex.message))
    #             _send_warning_email(context, ex)
    #             return ex.message
    return app


def _send_warning_email(ctx, exception):
    # from flask import current_app
    # import traceback
    # title = u'flask-base-plus-%s环境-告警通知' % current_app.config['CONFIG_NAME']
    # body = u'发现未处理flask-base-plus服务异常: \n{status}\n{message}'.format(status=ctx.get_service_status(), message=traceback.format_exc())
    # from axf_utils import email_util
    # email_util.send_warning_email(ctx, title, body, ['xxxxx@qq.com'])
    pass
