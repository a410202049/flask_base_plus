#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid

from axf_utils import to_str


class MemCache(object):
    local_cache = {}

    def __init__(self, expire_time=0):
        from . import get_client

        super(MemCache, self).__init__()
        self.expire_time = expire_time
        self.client = get_client()

    def set_expire_time(self, expire_time):
        self.expire_time = expire_time

    def get_expire_time(self):
        return self.expire_time

    def _get_inner_key(self, key):
        key = to_str(key)
        return (self.get_key_prefix() or '') + key

    def get(self, key):
        try:
            value = self.client.get(self._get_inner_key(key))
        except ValueError:
            # todo warning
            value = None
        return value

    def remove(self, key):
        return self.client.delete(self._get_inner_key(key))

    def set(self, key, value):
        return self.client.set(self._get_inner_key(key), value, self.expire_time), key

    def get_key_prefix(self):
        return None

if __name__ == '__main__':
    import bmemcached

    client = bmemcached.Client(
        servers=["a7fa9c3d3e6511e4.m.cnqdalicm9pub001.ocs.aliyuncs.com"],
        username="a7fa9c3d3e6511e4",
        password='366f_6dfc'
    )

    k = uuid.uuid1().hex
    v = 'seaman'
    print client.set(k, v, 60)
