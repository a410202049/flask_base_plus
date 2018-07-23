#!/usr/bin/python
# -*- encoding: utf-8 -*-
from ..context.context import Context


class ApiContext(Context):
    def __init__(self,
                 context=None,
                 name=None,
                 version=None,
                 service=None,
                 method=None,
                 customer_no=None):

        super(ApiContext, self).__init__(context)
        is_context_valid = context and isinstance(context, ApiContext)
        self.name = name or (context.name if is_context_valid else None)
        self.version = version or (context.version if is_context_valid else None)
        self.service = service or (context.service if is_context_valid else None)
        self.method = method or (context.method if is_context_valid else None)
        self.customer_no = customer_no or (context.customer_no if is_context_valid else None)

        from ..structed_log.api_log import ApiLog
        self.log = ApiLog(self)
