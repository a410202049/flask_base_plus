#!/usr/bin/python
# -*- encoding: utf-8 -*-
from . import BaseLog, LogType


class NetworkMethod(object):
    HttpGet = "GET",
    HttpPost = "POST"


class NetworkInLog(BaseLog):
    def __init__(self, context, ip, method, url):
        super(NetworkInLog, self).__init__(context)

        self.ip = ip
        self.method = method
        self.url = url

    def get_log_type(self):
        return LogType.NetworkIn

    def get_header(self):
        return u'%s[%s:%s:%s]' % (BaseLog.get_header(self), self.ip, self.method, self.url)


class NetworkOutLog(BaseLog):
    def __init__(self, context, method, url):
        super(NetworkOutLog, self).__init__(context)

        self.method = method
        self.url = url

    def get_log_type(self):
        return LogType.NetworkOut

    def get_header(self):
        return u'%s[%s:%s]' % (BaseLog.get_header(self), self.method, self.url)


