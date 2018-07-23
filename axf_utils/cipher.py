#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64

from Crypto.Cipher import AES, DES3


class Aes128(object):

    @classmethod
    def _pad(cls, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @classmethod
    def _unpad(cls, s):
        return s[:-ord(s[len(s) - 1:])]

    def __init__(self, key, mode=AES.MODE_CBC, iv=AES.block_size * '\x00'):
        self.key = key[:AES.block_size] if len(key) >= AES.block_size else (key + '\x00' * (AES.block_size - len(key)))
        self.mode = mode
        self.IV = iv

    def encrypt(self, data):
        cipher = AES.new(self.key, self.mode, self.IV)
        enc_data = cipher.encrypt(self._pad(data))

        return enc_data

    def decrypt(self, text):
        if len(text) % AES.block_size != 0:
            return None

        cipher = AES.new(self.key, self.mode, self.IV)
        data = self._unpad(cipher.decrypt(text))

        return data


class TripleDES(object):

    @classmethod
    def _pad(cls, s):
        return s + (DES3.block_size - len(s) % DES3.block_size) * chr(DES3.block_size - len(s) % DES3.block_size)

    @classmethod
    def _unpad(cls, s):
        return s[:-ord(s[len(s) - 1:])]

    def __init__(self, key, mode=DES3.MODE_CBC, iv=8 * '\x00'):
        self.key = key[:24]
        self.mode = mode
        self.IV = iv

    def encrypt(self, data):
        cipher = DES3.new(self.key, self.mode, self.IV)
        enc_data = cipher.encrypt(self._pad(data))

        return enc_data

    def decrypt(self, text):
        if len(text) % DES3.block_size != 0:
            return None

        cipher = DES3.new(self.key, self.mode, self.IV)
        data = self._unpad(cipher.decrypt(text))

        return data


if __name__ == '__main__':
    def test_3des():
        src = '001'
        enc_data = TripleDES('GomKBjwuzwB0tkL578OBr6CM', iv='12345678').encrypt(src)
        print len(enc_data)
        print base64.encodestring(enc_data)

    def test_aes128():
        aes = Aes128('dev_b4cab4f33afa805e5fd81c0f01465e3f')

        src = '6225880284991537'
        enc_data = aes.encrypt(src)
        dec_data = aes.decrypt(enc_data)

        print dec_data

    test_aes128()
    # print len(base64.decodestring('9fglVuUQAW8='))
