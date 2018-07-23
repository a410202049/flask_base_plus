#!/usr/bin/python
# -*- encoding: utf-8 -*-

import weakref
from logging import DEBUG, INFO, WARN, ERROR

import log
from .. import to_unicode
from log import get_log

import platform
CONFIG = dict(
    LOGGER_NAME='gen',
    LOGGING='DEBUG',
    LOG_FOLDER='./',
    LOG_FILE_PREFIX='gen_log',
    LOG_FILE_CONTAINS_HOSTNAME=False,
    LOG_FILE_MAX_SIZE=1024 * 1024,
    LOG_FILE_NUM_BACKUPS=10,
    LOG_TO_STDERR=True,
    LOCAL=False,
    HOSTNAME=platform.node(),
    MULTI_PROCESS=False,
    LOG_TO_FILE=True
)


def init_app(app):
    if app:
        for k in CONFIG.keys():
            if k in app.config:
                CONFIG[k] = app.config[k]


class LogType(object):
    General = 'GN'
    NetworkIn = 'NI'
    NetworkOut = 'NO'
    Route = 'RT'
    Service = 'SV'
    App = 'AP'
    Dao = 'DO'
    SysInterfaces = 'SI'
    Business = 'BS'
    AsyncTask = 'AT'


class BaseLog(object):
    def __init__(self, context):
        if context is None:
            raise RuntimeError('context is required')

        if hasattr(context, 'log') and context.log:
            self.gen_log = context.log.gen_log
        else:
            self.gen_log = get_log()

        self.r_context = weakref.ref(context)

    def d(self, msg, *args, **kwargs):
        self.log(DEBUG, msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        self.log(INFO, msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        self.log(WARN, msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.log(ERROR, msg, *args, **kwargs)

    def ex(self, msg, *args, **kwargs):
        kwargs['exc_info'] = 1

        self.e(msg, *args, **kwargs)

    def get_header(self):
        context = self.get_context()

        return u'[svid:%s:%s][sn:%s][tp:%s]' % (
            context.server_id if context else '-',
            context.service_id if context else '-',
            context.serial if context else '-',
            self.get_log_type())

    def log(self, level, msg, *args, **kwargs):
        msg = to_unicode(msg) if isinstance(msg, str) else msg
        header = self.get_header()

        self.gen_log.log(level, u'%s\t%s' % (header, msg), *args, **kwargs)

    def get_log_type(self):
        return LogType.General

    def get_context(self):
        return self.r_context()


class DaoLog(BaseLog):
    def __init__(self, context, dao_name, method_name):
        super(DaoLog, self).__init__(context)

        self.dao_name = dao_name
        self.method_name = method_name

    def get_log_type(self):
        return LogType.Dao

    def get_header(self):
        return u'%s\t[%s:%s]' % (BaseLog.get_header(self), self.dao_name, self.method_name)
