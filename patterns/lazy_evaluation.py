#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/6'
"""

from __future__ import print_function
import functools


class lazy_property(object):

    def __init__(self, function):
        self.function = function
        # what functools do
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    return _lazy_property


class Person(object):

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        relatives = "Many relatives"
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


if __name__ == '__main__':
    jhon = Person("Jhon", "Coder")
    print(u"Name: {0.name}  Occupation: {0.occupation}".format(jhon))
    print(u"Before we access `relatives`:")
    print(jhon.__dict__)
    print(u"Jhon's relatives: {0}".format(jhon.relatives))
    print(u"After we've accessed `relatives`:")
    print(jhon.__dict__)
    print(jhon.parents)
    print(jhon.__dict__)
    print(jhon.parents)
    print(jhon.call_count2)


