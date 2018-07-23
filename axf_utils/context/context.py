#!/usr/bin/python
# -*- encoding: utf-8 -*-
import uuid

from ..structed_log import BaseLog
from . import CONFIG


class Context(object):
    def __init__(self, context=None):
        # self.log = None
        if context:
            self.serial = context.serial
            self.server_type = context.server_type
            self.server_version = context.server_version
            self.server_id = context.server_id
            self.service_id = context.service_id
            self.hostname = context.hostname
            self.config_name = context.config_name
            self.version = context.version
        else:
            self.serial = uuid.uuid1().hex
            self.server_type = CONFIG['SERVER_TYPE']
            self.server_version = CONFIG['SERVER_VERSION']
            self.server_id = CONFIG['SERVER_ID']
            self.service_id = CONFIG['SERVICE_ID']
            self.hostname = CONFIG['HOSTNAME']
            self.config_name = CONFIG['CONFIG_NAME']
            self.version = CONFIG['VERSION']

        self.log = BaseLog(self)

    def get_service_status(self):
        return \
            '%s<br>' \
            'I\'m still alive.<br>' \
            '%s @ %s - %s using %s<br>' \
            'v%s' \
            % (self.serial, self.service_id, self.server_id, self.hostname, self.config_name, self.version)


class SystemContext(Context):

    def __init__(self):
        super(SystemContext, self).__init__()
        self.serial = 'system'
