#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/7'
"""

# lista 是可迭代对象
# listb 是迭代器


# from itertools import islice


# 构造一个迭代器 斐波那契数列
class Fib(object):

    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    # python 2
    def next(self):
        value = self.curr
        self.curr = self.curr + self.prev
        self.prev = value
        return value

    # 兼容python3
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


# 生成器版本
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


class MyIterator(object):

    def __init__(self, step):
        self.step = step

    def next(self):
        if self.step == 0:
            raise StopIteration
        else:
            self.step -= 1
        return self.step

    def __iter__(self):
        return self

def main():
    lista = [1, 2, 3]
    listb = iter(lista)
    print listb.next()
    print listb.next()
    print listb.next()
    print(id(lista))
    print(id(listb))
    # fib = Fib()
    # print(list(islice(fib(), 0, 10)))

    myiter = MyIterator(5)
    for item in myiter:
        print item

if __name__ == '__main__':
    main()

    # summary  迭代器是可迭代的实现了 __iter__ 和 __next__方法 python 2是 next()
    # 生成器表达式和含有yield的函数都是生成器对象 一定是可以迭代的
    # 生成器和迭代器可以节省内存 应该尽量使用