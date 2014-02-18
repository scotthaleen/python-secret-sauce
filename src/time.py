# -*- coding: utf-8 -*-
import datetime
import time


def fmtNow(pattern='%Y%m%d%H%M%S'):
    return datetime.datetime.utcnow().strftime(pattern)

def fmtNowISO():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

def epocTime(long_time):
    return datetime.datetime.fromtimestamp(long_time)

def epochTimeStr(long_time):
    return datetime.datetime.fromtimestamp(long_time).strftime('%Y-%m-%dT%H:%M:%S')

def parseStrTimeToEpoch(strTime, pattern):
    return time.mktime(time.strptime(strTime, pattern))

