#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '2017/12/4'
"""


from requests import get

# r = get(url='http://www.baidu.com')
# print(r.content)

# class Borg(object):
#     __shared_state = {}
#
#     def __init__(self):
#         self.__dict__ = self.__shared_state
#         self.state = 'Init'
#
#     def __str__(self):
#         return self.state
#
#
# class YourBorg(Borg):
#     pass
#
#
# if __name__ == '__main__':
#     rm1 = Borg()
#     rm2 = Borg()
#     rm1.state = 'Idle'
#     rm2.state = 'Running'
#     print("rm1: {}".format(rm1))
#     print("rm2: {}".format(rm2))
#
#     print('rm1 id: {0}'.format(id(rm1)))
#     print('rm2 id: {0}'.format(id(rm2)))
#
# from requests.models import AuthManager
#
# auth1 = AuthManager()
# auth1.add_password(realm=None, user='abc', passwd='abc', uri='http://www.baidu.com')
#
# auth2 = AuthManager()
# auth2.add_password(realm=None, user='abc1', passwd='abc1', uri='http://www.baidu.com')
# print(auth1.passwd)
# print(auth2.passwd)
# print(id(auth1))
# print(id(auth2))
import six
import abc
import random


class PetShop(object):
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory. We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We alse have {}".format(self.pet_factory.get_food()))


# stuff that our factory makes

class Dog(object):

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

# Factory classes


class DogFactory(object):

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory(object):

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create the proper family

def get_factory():
    """let's be dynamic"""
    return random.choice([DogFactory, CatFactory])()


@six.add_metaclass(abc.ABCMeta)
class Pet(object):

    @classmethod
    def from_name(cls, name):
        for sub_cls in cls.__subclasses__():
            if name == sub_cls.__name__.lower():
                return sub_cls()

    @abc.abstractmethod
    def speak(self):
        """"""


class Kitty(Pet):

    def speak(self):
        return "Miao"


class Duck(Pet):

    def speak(self):
        return "Quak"


if __name__ == '__main__':
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("="*20)

    for name in ['kitty', 'duck']:
        pet = Pet.from_name(name)
        print("{} : {}".format(name, pet.speak()))



