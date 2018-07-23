#!/usr/bin/python
# -*- encoding: utf-8 -*-
import collections
import functools
from datetime import datetime

CONFIG = {
    'ENCODING': 'utf-8'
}

_app = None


def init_app(app):
    print 'init app in axf util'
    if not app:
        return

    if 'ENCODING' in app.config:
        CONFIG['ENCODING'] = app.config['ENCODING']

    global _app
    _app = app


def get_app():
    return _app


def to_unicode(data, encoding=None):
    if data is None:
        return u'None'

    if isinstance(data, basestring):
        if not isinstance(data, unicode):
            return unicode(data, encoding or CONFIG['ENCODING'])
        else:
            return data
    elif isinstance(data, collections.Mapping):
        return dict(map(to_unicode, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(to_unicode, data))
    else:
        return data


def to_str(data, encoding=None):
    if isinstance(data, unicode):
        return data.encode(encoding or CONFIG['ENCODING'])
    elif isinstance(data, basestring):
        return data
    elif isinstance(data, collections.Mapping):
        return dict(map(to_str, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(to_str, data))
    else:
        return data


def convert_api_version_to_pkg_name(api_version):
    return 'v%s' % api_version.replace('.', '_')


ascii_0 = ord('0')
ascii_9 = ord('9')


def is_numic(text):

    for c in text:
        val = ord(c)
        if not (ascii_0 <= val <= ascii_9):
            return False

    return True


def cal_id_card_no_verify_code(id_card_no):
    weitht = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    verify_codes = '10X98765432'

    sum = 0
    for i, c in enumerate(id_card_no[:17]):
        sum += (ord(c) - ascii_0) * weitht[i]

    return verify_codes[sum % 11]


def verify_id_card_no(id_card_no):
    if not id_card_no or len(id_card_no) != 18:
        return False

    district = id_card_no[:6]
    year = id_card_no[6:10]
    month = id_card_no[10:12]
    day = id_card_no[12:14]
    appendix = id_card_no[14:17]
    verify = id_card_no[-1].upper()

    if not is_numic(id_card_no[:-1]):
        return False

    year = int(year)
    if not (1900 < year < 2900):
        return False

    month = int(month)
    if not (1 <= month <= 12):
        return False

    day = int(day)
    if not(1 <= day <= 31):
        return False

    my_verify = cal_id_card_no_verify_code(id_card_no)

    return my_verify == verify


def ignore_exception(exc=None):
    """
    ignore exception
    :param exc: except
    """
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except Exception, ex:
                if exc and not isinstance(ex, exc):
                    raise
                else:
                    from axf_utils.context.context import Context
                    Context().log.ex(u'found exception and ignored: method - [%s] exception - [%s] message - [%s]' %
                                     (func.func_name, ex.__class__.__name__, to_unicode(ex.message)))
                    pass

        return wrapper

    return decorator


def luhn_check(num):
    num = str(num)

    digits = [int(x) for x in reversed(num)]
    check_sum = sum(digits[::2]) + sum((dig // 10 + dig % 10) for dig in [2 * el for el in digits[1::2]])

    return check_sum % 10 == 0


def str2datetime(str_date):
    if isinstance(str_date, datetime):
        return str_date

    year = int(str_date[:4]) if len(str_date) >= 4 else 0
    month = int(str_date[4:6]) if len(str_date) >= 6 else 0
    day = int(str_date[6:8]) if len(str_date) >= 8 else 0
    hour = int(str_date[8:10]) if len(str_date) >= 10 else 0
    minute = int(str_date[10:12]) if len(str_date) >= 12 else 0
    second = int(str_date[12:14]) if len(str_date) >= 14 else 0

    return datetime(year, month, day, hour, minute, second)


if __name__ == '__main__':
    def test_to_str():
        str_val1 = u'U中文字串'
        str_val2 = u'Uenglish string'
        str_val3 = '中文字串'
        str_val4 = 'english string'
        map_val = {
            u'U关键字': u'值',
            u'Ukey': u'Uvalue',
            '关键字': '值',
            'key': 'value',
            u'U列表关键字': [u'U列表值1', u'U列表值2', u'U列表值3',],
            u'Ulist_key': [u'Uvalue1', u'Uvalue2', u'Uvalue3',],
            '列表关键字': ['列表值1', '列表值2', '列表值3',],
            'list_key': ['value1', 'value2', 'value3',],
            u'U字典关键字': {u'U字典关键字A': u'U字典值A'},
            u'Udict_key': {u'Udict_keyA': u'UvalueA'},
            '字典关键字': {'字典关键字A': '字典值A'},
            'dict_key': {'dict_keyA': 'valueA'},
        }

        print to_str(str_val1)
        print to_str(str_val2)
        print to_str(str_val3)
        print to_str(str_val4)
        print to_str(map_val)


    def test_to_unicode():
        str_val1 = u'U中文字串'
        str_val2 = u'Uenglish string'
        str_val3 = '中文字串'
        str_val4 = 'english string'
        map_val = {
            u'U关键字': u'值',
            u'Ukey': u'Uvalue',
            '关键字': '值',
            'key': 'value',
            u'U列表关键字': [u'U列表值1', u'U列表值2', u'U列表值3',],
            u'Ulist_key': [u'Uvalue1', u'Uvalue2', u'Uvalue3',],
            '列表关键字': ['列表值1', '列表值2', '列表值3',],
            'list_key': ['value1', 'value2', 'value3',],
            u'U字典关键字': {u'U字典关键字A': u'U字典值A'},
            u'Udict_key': {u'Udict_keyA': u'UvalueA'},
            '字典关键字': {'字典关键字A': '字典值A'},
            'dict_key': {'dict_keyA': 'valueA'},
        }

        print to_unicode(str_val1)
        print to_unicode(str_val2)
        print to_unicode(str_val3)
        print to_unicode(str_val4)
        print to_unicode(map_val)


    # test_to_unicode()
    def test_ignore_exception():
        @ignore_exception(RuntimeError)
        def raise_exception(exc_type):
            raise exc_type('test exception')

        @ignore_exception((SystemError, RuntimeError))
        def raise_exception2(exc_type):
            raise exc_type('test exception')

        try:
            raise_exception(RuntimeError)
        except Exception, ex:
            print ex
        try:
            raise_exception(SystemError)
        except Exception, ex:
            print ex
        try:
            raise_exception(ImportError)
        except Exception, ex:
            print ex
        try:
            raise_exception2(RuntimeError)
        except Exception, ex:
            print ex
        try:
            raise_exception2(SystemError)
        except Exception, ex:
            print ex
        try:
            raise_exception2(ImportError)
        except Exception, ex:
            print ex

    test_ignore_exception()


def to_safe_bank_card_no(bank_card_no):
    if len(bank_card_no) <= 4:
        bank_card_no = '*' * (4 - len(bank_card_no)) + bank_card_no
    else:
        bank_card_no = bank_card_no[-4:]

    return bank_card_no


def to_safe_name(name):
    if len(name) == 1:
        return '*' + name
    elif len(name) == 2:
        return '*' + name[-1]
    elif len(name) > 2:
        return name[0] + '*' * (len(name) - 2) + name[-1]
    else:
        return name


def to_safe_id_card_no(id_card_no):
    if len(id_card_no) <= 3:
        id_card_no = '*' * (3 - len(id_card_no)) + id_card_no
    else:
        id_card_no = id_card_no[-3:]

    return id_card_no


def amt_fmt2axf(amt):
    if amt is None:
        return None

    if amt == '':
        return '0.00'

    amt = float(amt)

    return '%.2f' % amt


def amt_up2axf(amt):
    if amt is None:
        return amt

    amt = int(amt)
    amt = amt / 100.0

    return '%.2f' % amt


def amt_axf2up(amt):
    if amt is None:
        return amt

    amt = float(amt)

    return str(int(round(amt * 100.0)))

