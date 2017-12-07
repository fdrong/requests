#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/7'
"""


class HelloMeta(type):

    def __new__(cls, name, bases, attrs):

        def __init__(cls, func):
            cls.func = func

        def hello(cls):
            print "hello world"

        t = type.__new__(cls, name, bases, attrs)
        t.__init__ = __init__
        t.hello = hello
        return t


class New_Hello(object):
    __metaclass__ = HelloMeta


hello = New_Hello(lambda x:x/2)
print(type(hello))
print(hello.func(4))
hello.hello()
