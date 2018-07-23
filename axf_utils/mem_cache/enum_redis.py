#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import


class EnumRedis(object):
    """
    内存缓存
    """
    def __init__(self):
        self.cache = dict()
        super(EnumRedis, self).__init__()

    def exists(self, session_id):
        """
        校验是否存在该session_id
        :param session_id:
        :return:
        """
        is_exists = True if session_id in self.cache else False
        return is_exists

    def hset(self, session_id, key, value):
        """
        设置session相关的key-value值
        :param session_id:
        :param key:
        :param value:
        :return:
        """
        if session_id in self.cache:
            current_session = self.cache.get(session_id)

            if isinstance(current_session, dict):
                current_session.update({key: value})
        else:
            self.cache.update({session_id: {key: value}})

    def expire(self, session_id, expire_time):
        """
        延长session的有效期
        :param session_id:
        :param expire_time:
        :return:
        """
        pass

    def hget(self, session_id, key):
        """
        获取session的key对应的值
        :param session_id:
        :param key:
        :return:
        """
        current_session = self.cache.get(session_id, None)

        if isinstance(current_session, dict):
            return current_session.get(key)
        return None

    def hdel(self, session_id, key):
        """
        删除session对应的值
        :param session_id:
        :param key:
        :return:
        """
        current_session = self.cache.get(session_id)

        if isinstance(current_session, dict) and key in current_session:
            current_session.pop(key)
            return True
        return False

    def delete(self, session_id):
        current_session = self.cache.get(session_id)

        if isinstance(current_session, dict):
            self.cache.pop(session_id)
            return True
        return False
