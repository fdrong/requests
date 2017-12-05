#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/5'
"""


# Director
class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# Builder
class Builder(object):

    def __init__(self):
        self.building = None

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def new_building(self):
        self.building = Building()


class HouseBuilder(Builder):

    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class FlatBuilder(Builder):

    def build_size(self):
        self.building.size = 'Small'

    def build_floor(self):
        self.building.floor = 'Many'


class Building(object):

    def __init__(self):
        self.size = None
        self.floor = None

    def __repr__(self):
        return "Size: {0.size} | floor: {0.floor}".format(self)

if __name__ == '__main__':
    director = Director()
    director.builder = HouseBuilder()
    director.construct_building()
    print(director.get_building())




