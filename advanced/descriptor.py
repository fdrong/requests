#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/7'
"""


class Mydescriptor(object):
    _value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        print("setting value")
        self._value = value.upper()


class Test(object):
    my = Mydescriptor()
    test2 = 'abcde'


test = Test()
test.my = 'hello world'
print test.my
print test.__dict__


def test2():
    pass

print(dir(test2))

# 对类的属性修改的一种劫持
# 函数也是也是描述符


# 一个开源实现

class _Missing(object):

    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'

_missing = _Missing()


class cached_property(object):

    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


