#!/usr/bin/python
# -*- encoding: utf-8 -*-
from datetime import datetime

from axf_utils.enum_util import BaseEnum


class RecordType(BaseEnum):
    START = 1
    PAUSE = 2
    RECORD = 3
    RESET = 4


class Record(object):

    def __init__(self, record_type, start_time, rel_start_time, current_time, message):
        super(Record, self).__init__()

        self.record_type = record_type
        self.start_time = start_time
        self.rel_start_time = rel_start_time
        self.current_time = current_time
        self.message = message

    def get_time_from_start(self):
        return self.current_time - self.start_time

    def get_time_from_rel_start(self):
        return self.current_time - self.rel_start_time

    def get_time_from(self, record):
        return self.current_time - record.current_time


class StopWatchStatus(BaseEnum):
    PENDING = 0
    RUNNING = 1
    PAUSED = 2


class StopWatch(object):

    def __init__(self):
        super(StopWatch, self).__init__()

        self._records = []
        self.status = StopWatchStatus.PENDING

        self.start_time = None
        self.rel_start_time = None
        self.pause_time = None
        self.status = None

        self._reset_status()

    def _reset_status(self):
        self.start_time = None
        self.rel_start_time = None
        self.pause_time = None
        self.status = StopWatchStatus.PENDING

    def _inner_record(self, record_type, message):
        record = Record(record_type, self.start_time, self.rel_start_time, datetime.now(), message)
        self._records.append(record)

        return record

    def start(self, message=None):
        if self.status == StopWatchStatus.PENDING:
            self.start_time = self.rel_start_time = datetime.now()
        elif self.status == StopWatchStatus.PAUSED:
            self.rel_start_time = datetime.now() - self.pause_time
            self.pause_time = None
        else:
            raise RuntimeError('illegal stop watch status %s for start' % StopWatchStatus.get_name(self.status))

        self.status = StopWatchStatus.RUNNING

        return self._inner_record(RecordType.START, message)

    def pause(self, message=None):
        if self.status == StopWatchStatus.RUNNING:
            self.pause_time = datetime.now()
        else:
            raise RuntimeError('illegal stop watch status %s for pause' % StopWatchStatus.get_name(self.status))

        self.status = StopWatchStatus.PAUSED
        return self._inner_record(RecordType.PAUSE, message)

    def record(self, message=None):
        if self.status != StopWatchStatus.RUNNING:
            raise RuntimeError('illegal stop watch status %s for record' % StopWatchStatus.get_name(self.status))

        return self._inner_record(RecordType.RECORD, message)

    def reset(self, message=None):
        if self.status != StopWatchStatus.PAUSED:
            raise RuntimeError('illegal stop watch status %s for reset' % StopWatchStatus.get_name(self.status))

        result = self._inner_record(RecordType.RESET, message)
        self._reset_status()

        return result

    def get_records(self):
        return self._records
