#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import base64

from Crypto.Cipher import DES3
from binascii import a2b_hex, b2a_hex

from test.unit.base import BaseTestCase
from Crypto import Random
from utils.desutils import Des3FileUtils
from utils.fileutils import FileUtils

BS = 8
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s)-1:])]

class Des3FileUtilsTestCase(BaseTestCase):
    """
    Des3FileUtilsTestCase
    iconv -f UTF-8 -t GB2312 IMGDOC0001_AXF_20180507_0001B.txt > IMGDOC0001_AXF_20180507_0001.txt
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_padding(self):
        a = '12345678'
        b = '123'
        c = '1234567890'

        print len(pad(a))
        print len(pad(b))
        print len(pad(c))

        print ord(pad(a)[-1])
        print ord(pad(b)[-1])
        print ord(pad(c)[-1])

    def test_encrypt_file(self):
        file_path = '/Users/apple/PycharmProjects/workspace/axf_library/library/utils/tests/pic.zip'
        # file_path = '/Users/apple/PycharmProjects/workspace/axf_library/library/utils/tests/new.txt'
        with open(file_path, 'rb') as this_file:
            content = this_file.read()
        print content
        content = base64.b64encode(content)
        # content = content.replace('\n', '')

        key = '132e8a57b4f6139b3a5de9g4'

        des3 = DES3.new(key, DES3.MODE_ECB)
        content = pad(content)
        content = des3.encrypt(content)
        content = base64.encodestring(content)

        with open('./IMGDOC0001_AXF_20180514_0001.zip', 'wb') as out_file:
        # with open('./encrypt_new.txt', 'wb') as out_file:
            out_file.write(content)
        print 'ok'

    def test_decrypt_file(self):
        content = FileUtils.read_all_data(
            '/Users/apple/PycharmProjects/workspace/axf_library/library/utils/tests/J_CBIB0020_AXF_20180605.zip')
        # content = base64.decodestring(content)
        # print content
        # print b2a_hex(content)
        key = '132e8a57b4f6139b3a5de9g4'
        # Des3FileUtils.encrypt_file("/Users/apple/liaoshanqing/tmp/test_file_crypt.txt",
        #                            '/Users/apple/liaoshanqing/tmp/test_file_crypt_1.txt', 8192, key, iv)
        # Des3FileUtils.decrypt_file('./IMGDOC0001_AWX_20170724_0002.zip',
        #                            './axf_test.zip', 8192, key)
        des3 = DES3.new(key, DES3.MODE_ECB)
        with open('./1.txt', 'wb') as out_file:
            result = des3.decrypt(content)
            # print result
            # result = base64.decodestring(result)
            # print result.decode('gbk')
            # print b2a_hex(result)
            out_file.write(result)
        print 'ok'


