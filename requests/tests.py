#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/4'
"""


from requests import get

r = get(url='http://www.baidu.com')
print(r.content)