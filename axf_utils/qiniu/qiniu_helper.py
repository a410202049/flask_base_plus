#!/usr/bin/env python
# -*- coding:utf-8 -*-
from axf_utils.qiniu import config
from qiniu import Auth
from qiniu import BucketManager


class QiniuUtil(object):
    def __init__(self):
        self.__auth = Auth(config['QINIU_CONF_ACCESS_KEY'], config['QINIU_CONF_SECRET_KEY'])
        super(QiniuUtil, self).__init__()

    def upload_token(self, key=None):
        return self.__auth.upload_token(config['QINIU_BUCKET_NAME'], key=key)

    def private_download_url(self, key, expires=3600):
        return self.__auth.private_download_url(config['QINIU_DOMAIN'] + key, expires=expires)

    @staticmethod
    def public_download_url(key):
        return 'http://' + '/'.join([config['QINIU_DOMAIN'], key])

    def remove_file(self, key):
        bucket_manager = BucketManager(self.__auth)
        ret, info = bucket_manager.delete(config['QINIU_BUCKET_NAME'], key)
        if info.status_code == 200:
            return True, u'删除成功'
        else:
            return False, u'删除失败 %r' % info


