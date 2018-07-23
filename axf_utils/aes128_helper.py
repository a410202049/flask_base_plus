#!/usr/bin/python
# -*- coding: utf-8 -*-

from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s)-1:])]

class PrpCrypt(object):
    def __init__(self, key):
        self.key = key[:16]
        self.mode = AES.MODE_CBC
        self.IV = 16 * '\x00'

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self,data):
        encryptor_deb = AES.new(self.key, self.mode, self.IV)
        ciphertext = encryptor_deb.encrypt(pad(data))
        return b2a_hex(ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.IV)
        plain_text = unpad(cryptor.decrypt(a2b_hex(text)))
        return plain_text


if __name__ == '__main__':

    a = PrpCrypt('b4cab4f33afa805e')
    print a.encrypt('6217976510002841858')
    print a.decrypt('4669a9c9665b3170dc6c8d9eacd1ad44156ea9e76201caffc96b53b6db6b2222')