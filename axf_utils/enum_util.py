#!/usr/bin/python
# -*- coding: utf-8 -*-


class BaseEnum(object):
    @classmethod
    def names(cls):
        return [name for name in dir(cls) if not name.startswith('_') and name not in ['get_name','names','value_of','values']]

    @classmethod
    def values(cls):
        return [getattr(cls, name) for name in dir(cls) if not name.startswith('_') and name not in ['get_name','names','value_of','values']]

    @classmethod
    def get_name(cls, value, default_name=None):
        for name in cls.names():
            if getattr(cls, name) == value:
                return name

        return default_name

    @classmethod
    def value_of(cls, name, default_value=None):
        if name in cls.names():
            return getattr(cls, name)

        return default_value
