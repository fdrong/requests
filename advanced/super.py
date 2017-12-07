#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/7'
"""


import collections


class LoggingDict(dict):

    def __setitem__(self, key, value):

        print("Settingto %s %s" % (key, value))
        super(LoggingDict, self).__setitem__(key, value)


class LoggingOD(LoggingDict, collections.OrderedDict):
    pass


a = LoggingDict()
a['a'] = 'a'
a['b'] = 'b'


class Shape(object):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super(Shape, self).__init__(**kwargs)