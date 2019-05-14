# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:51
# @Author  : zdRan
# @FileName: polymorphism.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

# 多态

class Animal:
    def run(self):
        raise AttributeError("子类必须实现")


class Person(Animal):
    def run(self):
        print("人走")


class Pig(Animal):
    def run(self):
        print("Pig run")


class Dog(Animal):
    def run(self):
        print("Dog run")


# 多态性

def func(obj):
    obj.run()


func(Dog())