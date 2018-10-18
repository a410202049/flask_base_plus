# coding: utf-8
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy, get_debug_queries, BaseQuery
from flask_login import LoginManager

from axf_utils.context.context import Context
from axf_utils.exception import AxBaseException
from app.utils.restful_response import CommonResponse, ResultType
from config import config
import datetime
from flask import render_template, request, jsonify
from werkzeug.utils import import_string

import time
from app.utils.log import FinalLogger

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# mail = Mail()

#设置db.session.query 可以使用分页类
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
    #注册蓝图
    blueprints = [
        "app.controller.admin:admin"
    ]
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    app.config['MAX_CONTENT_LENGTH'] = app.config.get('MAX_CONTENT_LENGTH')
    #开启调试模式
    app.debug = app.config.get('DEBUG')

    # jinja2 None to ''
    app.jinja_env.finalize = finalize
    
    #配置log路径
    log_handler = FinalLogger(app).getLogger()
    app.logger.addHandler(log_handler)

    import axf_utils
    axf_utils.init_app(app)

    from app import template_filter
    template_filter.init_app(app)

    #注册蓝图
    register_blueprints(app)

    #添加当前时间戳 全局变量
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


    @app.errorhandler(403)
    def forbidden(e):
        if request.accept_mimetypes.accept_json and \
                not request.accept_mimetypes.accept_html:
            response = jsonify({'error': 'forbidden'})
            response.status_code = 403
            return response
        return render_template('403.html'), 403


    @app.errorhandler(404)
    def page_not_found(e):
        if request.accept_mimetypes.accept_json and \
                not request.accept_mimetypes.accept_html:
            response = jsonify({'error': 'not found'})
            response.status_code = 404
            return response
        return render_template('404.html'), 404


    @app.errorhandler(500)
    def internal_server_error(e):
        if request.accept_mimetypes.accept_json and \
                not request.accept_mimetypes.accept_html:
            response = jsonify({'error': 'internal server error'})
            response.status_code = 500
            return response
        return render_template('500.html'), 500


    @app.errorhandler(Exception)
    def handle_exception(ex):
        if current_app.config['CONFIG_NAME'] != 'local':
            if not isinstance(ex, AxBaseException):
                context = Context()
                context.log.e('notify handle error: {0}'.format(ex.message))
                _send_warning_email(context, ex)
                return ex.message

    # @app.errorhandler(AxBaseException)
    # def exception_error_handler(e):
    #     app.logger.warning('%s %s' % (e.error_msg, e))
    #     resp = {}
    #     base_resp = {}
    #     resp['resp_code'] = e.error_code
    #     resp['resp_msg'] = e.error_msg
    #     resp['timestamp'] =  int(round(time.time() * 1000))
    #     base_resp['resp'] = resp
    #     return jsonify(resp=resp),200

    # @app.template_filter("omit")
    # def omit(data, length):
    #     if len(data) > length:
    #         return data[:length-3] + '...'
    #     return data
    #
    # @app.template_filter("friendly_time")
    # def friendly_time(date):
    #     delta = datetime.datetime.now() - date
    #     if delta.days >= 365:
    #         return u'%d年前' % (delta.days / 365)
    #     elif delta.days >= 30:
    #         return u'%d个月前' % (delta.days / 30)
    #     elif delta.days > 0:
    #         return u'%d天前' % delta.days
    #     elif delta.seconds < 60:
    #         return u"%d秒前" % delta.seconds
    #     elif delta.seconds < 60 * 60:
    #         return u"%d分钟前" % (delta.seconds / 60)
    #     else:
    #         return u"%d小时前" % (delta.seconds / 60 / 60)
    #
    # @app.template_filter("format_article_time")
    # def format_article_time(date):
    #     return date.strftime('%m月%d日 %Y')

    return app


def _send_warning_email(ctx, exception):
    from flask import current_app
    import traceback

    title = u'flask-base-plus-%s环境-告警通知' % current_app.config['CONFIG_NAME']
    body = u'发现未处理flask-base-plus服务异常: \n{status}\n{message}'.format(status=ctx.get_service_status(), message=traceback.format_exc())
    from axf_utils import email_util
    email_util.send_warning_email(ctx, title, body, ['xxxxx@qq.com'])