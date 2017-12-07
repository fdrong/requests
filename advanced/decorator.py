#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/7'
"""


class Common(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("args: {}".format(args))
        self.func(*args, **kwargs)


@Common
def test(str1):
    print str1


def drinkable(message):
    def wrapper(cls):
        def drink(self):
            print("I can drink {}".format(message))
        cls.drink = drink
        return cls
    return wrapper


@drinkable("name")
class Person(object):
    name = 'abc'

p = Person()
p.drink()