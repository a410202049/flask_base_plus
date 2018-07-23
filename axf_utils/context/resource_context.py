#!/usr/bin/python
# -*- encoding: utf-8 -*-
from context import Context
from ..db_sessions import DBSessionForRead, DBSessionForWrite


class ResourceContext(Context):
    def __init__(self,
                 context=None,
                 base_path=None,
                 path=None,
                 method=None,
                 req_ip=None,
                 req_host=None
                 ):

        super(ResourceContext, self).__init__(context)

        is_context_valid = context and isinstance(context, ResourceContext)

        self.method = method or (context.method if is_context_valid else None)
        self.req_ip = req_ip or (context.req_ip if is_context_valid else None)
        self.base_path = base_path or (context.base_path if is_context_valid else None)
        self.path = path or (context.path if is_context_valid else None)
        self.req_host = req_host or (context.req_host if is_context_valid else None)

        from ..structed_log.resource_log import ResourceLog
        self.log = ResourceLog(self)

    def open_readable_db_sesion(self):
        return DBSessionForRead()

    def open_writable_db_sesion(self):
        return DBSessionForWrite()


