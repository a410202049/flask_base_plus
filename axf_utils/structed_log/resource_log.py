#!/usr/bin/python
# -*- encoding: utf-8 -*-
from axf_utils.context.resource_context import ResourceContext
from . import BaseLog, LogType


class ResourceLog(BaseLog):
    def __init__(self, resource_context):
        super(ResourceLog, self).__init__(resource_context)

        if not isinstance(resource_context, ResourceContext):
            raise RuntimeError('expect ResourceContext but got %s' % resource_context.__class__)

    def get_header(self):
        context = self.get_context()
        return u'{base_header}[{host}{base_path}{path}:{method}]'.format(
            base_header=super(ResourceLog, self).get_header(),
            host=context.req_host if context else '-',
            base_path=context.base_path if context else '-',
            path=context.path if context else '-',
            method=context.method if context else '-',
        )

    def get_log_type(self):
        return LogType.App
