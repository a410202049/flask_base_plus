#!/usr/bin/python
# -*- encoding: utf-8 -*-

from . import to_str, to_unicode


class AxBaseException(Exception):
    def __init__(self, error_msg, error_code, error_data=None):
        if not isinstance(error_code, (int, basestring)) and not isinstance(error_msg, basestring):
            raise RuntimeError(
                u'error_code is required as (int, basestring) and error_msg is required as basestring, but got(%s, %s)'
                % (type(error_code), type(error_msg)))

        error_code = to_unicode(error_code)
        error_msg = to_unicode(error_msg)

        super(AxBaseException, self).__init__(error_msg)

        self.error_code = error_code
        self.error_msg = error_msg
        self.error_data = error_data
