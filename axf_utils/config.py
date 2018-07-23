#!/usr/bin/python
# -*- encoding: utf-8 -*-


class BaseConfig(object):
    @classmethod
    def from_map(cls, mapping):
        prefix = getattr(cls, '__prefix__', '').upper()

        for k in cls.__dict__:
            if not 'k'.startswith('_') and k.isupper():
                k = prefix + k
                if k in mapping:
                    setattr(cls, k, mapping[k])

    @classmethod
    def from_obj(cls, obj):
        cls.from_map(obj.__dict__)
