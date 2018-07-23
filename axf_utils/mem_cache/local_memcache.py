#!/usr/bin/python
# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta


class LocalMemcache(object):
    def __init__(self):
        self.mapper = {}

    def _cal_expire_datetime(self, time=0):
        if time:
            return datetime.now() + timedelta(seconds=time)

        return None

    def _key_valid(self, key):
        item = self.mapper.get(key, None)
        if item:
            remain_time = item[1] - datetime.now()
            if remain_time.total_seconds() > 0:
                return True

        return False

    def set(self, key, value, time=0):
        self.mapper[key] = (value, self._cal_expire_datetime(time))
        return True

    def add(self, key, value, time=0):
        if key not in self.mapper:
            return self.set(key, value, time)

    def get(self, key):
        if self._key_valid(key):
            return self.mapper.get(key)[0]

    def replace(self, key, value, time=0):
        if self._key_valid(key):
            return self.set(key, value, time)

    def delete(self, key):
        self.mapper.pop(key, None)

        return True

    def delete_multi(self, keys):
        deleted = []
        for k in keys:
            deleted.append(self.delete(k))

        return deleted

    def get_multi(self, keys):
        result = []
        for k in keys:
            result.append(self.get(k))

        return result

    def set_multi(self, mappings, time=0):
        result = []
        for k in mappings:
            result.append(self.set(k, mappings[k], time))

        return True