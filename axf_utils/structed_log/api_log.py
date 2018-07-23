#!/usr/bin/python
# -*- encoding: utf-8 -*-
from ..context.api_context import ApiContext
from . import BaseLog, LogType


class ApiLog(BaseLog):
    def __init__(self, app_context):
        super(ApiLog, self).__init__(app_context)

        if not isinstance(app_context, ApiContext):
            raise RuntimeError('expect AppContext but got %s' % app_context.__class__)

    def get_header(self):
        context = self.get_context()
        return u'%s[%s\%s\%s\%s]' % \
               (super(ApiLog, self).get_header(),
                context.name if context else '-',
                context.version if context else '-',
                context.service if context else '-',
                context.method if context else '-')

    def get_log_type(self):
        return LogType.App
