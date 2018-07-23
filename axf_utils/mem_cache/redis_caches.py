#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

import time
import os
import six
import abc
from . import get_client
from hashlib import sha1, md5


@six.add_metaclass(abc.ABCMeta)
class BaseSession(object):
    """
    redis session
    """
    def __init__(self, secret_key, expire_time=0):
        self._redis = get_client()
        self._secret_key = secret_key
        self._expire_time = expire_time

    @abc.abstractmethod
    def init_session(self):
        pass


class DeviceSession(BaseSession):
    """
    设备session
    """
    _cus_sid_prefix = '_cust_session:'
    _device_sid_prefix = '_device_session:'
    _customer_session_expire_time_increment = 60

    def __init__(self, secret_key, expire_time=0):
        super(DeviceSession, self).__init__(secret_key, expire_time)
        self._customer_sid = None
        self._device_id = None
        self.customer_sid = None
        self.device_id = None

    def init_session(self):
        """
        初始化设备session
        """
        self.device_id = self.generate_device_session_id()
        self._device_id = ''.join([self._device_sid_prefix, self.device_id])
        self._redis.hset(self._device_id, 'last_active_time', time.time())
        self._redis.expire(self._device_id, self._expire_time)

    def init_customer_session(self, regist_serial):
        """
        初始化用户session
        """
        self.customer_sid = self.generate_customer_session_id(regist_serial)
        self._customer_sid = ''.join([self._cus_sid_prefix, self.customer_sid])
        self._redis.hset(self._customer_sid, 'lastActive', time.time())
        self._redis.hset(self._customer_sid, 'is_time_out', 0)

        if self._expire_time == 0:
            self._redis.expire(self._customer_sid, self._expire_time)
        else:
            self._redis.expire(self._customer_sid, self._expire_time + self._customer_session_expire_time_increment)

    def generate_device_session_id(self):
        """
        生成一个设备session
        """
        session_id = None
        while True:
            rand = os.urandom(16)
            now = time.time()
            session_id = md5("%s%s%s" % (rand, now, self._secret_key))
            session_id = session_id.hexdigest()
            if not self._redis.exists(self._device_sid_prefix + session_id):
                break
        return session_id

    def generate_customer_session_id(self, regist_serial):
        """
        生成一个用户session
        """
        session_id = md5("%s%s" % (self._secret_key, regist_serial))
        session_id = session_id.hexdigest()
        return session_id

    def set(self, regist_serial, device_name):
        """
        设置设备session
        :param regist_serial:
        :param device_name:
        :return:
        """
        self.init_session()
        customer_session_id = self.generate_customer_session_id(regist_serial)
        _customer_sid = ''.join([self._cus_sid_prefix, customer_session_id])

        if self._redis.exists(_customer_sid):
            self._redis.hset(_customer_sid, device_name, self._device_id)
        else:
            self.init_customer_session(regist_serial)
            self._redis.hset(self._customer_sid, device_name, self._device_id)

        self._redis.hset(self._device_id, 'device', device_name)
        self._redis.hset(self._device_id, 'regist_serial', regist_serial)
        return self.device_id, customer_session_id

    def get_device_session(self, device_session, key):
        _device_id = ''.join([self._device_sid_prefix, device_session])
        try:
            if device_session and self._redis.exists(_device_id):
                regist_serial = self._redis.hget(_device_id, 'regist_serial')
                if regist_serial:
                    _customer_sid = ''.join([self._cus_sid_prefix, self.generate_customer_session_id(regist_serial)])
                    if self._redis.exists(_customer_sid):
                        if self._expire_time == 0:
                            self._redis.expire(_customer_sid, self._expire_time)
                        else:
                            self._redis.expire(_customer_sid,
                                               self._expire_time + self._customer_session_expire_time_increment)
                        self._redis.expire(self._device_id, self._expire_time)
                else:
                    self._redis.delete(_device_id)
            value = self._redis.hget(''.join([self._device_sid_prefix, device_session]), key)
        except ValueError:
            value = None
        return value

    def get_customer_session(self, regist_serial, key):
        try:
            if key in ['Android', 'iOS']:
                key = 'app'
            _customer_sid = ''.join([self._cus_sid_prefix, self.generate_customer_session_id(regist_serial)])
            value = self._redis.hget(_customer_sid, key)
        except ValueError:
            value = None
        return value

    def remove(self, device_session):
        self._redis.delete(''.join([self._device_sid_prefix, device_session]))

    def remove_customer_session(self, customer_session):
        return self._redis.delete(''.join([self._cus_sid_prefix, customer_session]))

    def reset_customer_session(self, regist_serial, device_name, device_session):
        try:
            if device_name in ['Android', 'iOS']:
                device_name = 'app'
            customer_session_id = self.generate_customer_session_id(regist_serial)
            _customer_sid = ''.join([self._cus_sid_prefix, customer_session_id])

            if self._redis.exists(_customer_sid):
                self._redis.delete(_customer_sid)

            self.init_customer_session(regist_serial)
            self._redis.hset(self._customer_sid, device_name, ''.join([self._device_sid_prefix, device_session]))
        except Exception:
            return False
        return True
