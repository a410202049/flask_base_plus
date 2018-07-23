#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from datetime import datetime


def date2str(input_date):
    return input_date.strftime('%Y%m%d')


def str2date(input_str):
    return datetime.strptime(input_str, '%Y%m%d').date()


def datetime2str(input_datetime):
    return input_datetime.strftime('%Y%m%d%H%M%S')


def str2datetime(input_str):
    return datetime.strptime(input_str, '%Y%m%d%H%M%S')


def timestamp_to_strtime(timestamp):
    if isinstance(timestamp, unicode):
        timestamp = float(timestamp)
    local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    return local_str_time

def timestamp_to_format_datetime(timestamp):
    if isinstance(timestamp, unicode):
        timestamp = float(timestamp)
    local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
    return local_str_time

def timestamp_to_datetime(timestamp):
    if isinstance(timestamp, unicode):
        timestamp = float(timestamp)
    local_dt_time = datetime.fromtimestamp(timestamp / 1000.0)
    return local_dt_time


def datetime_to_strtime(datetime_obj):
    local_str_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    return local_str_time


def datetime_to_timestamp(datetime_obj):
    local_timestamp = long(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    return local_timestamp


if __name__ == '__main__':
    a = str2date('201604')
