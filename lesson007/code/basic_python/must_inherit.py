# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:31
# @Author  : zdRan
# @FileName: must_inherit.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
from abc import ABCMeta, abstractmethod


class Tester(metaclass=ABCMeta):

    @abstractmethod
    def test(self):
        pass

class FunctionTester(Tester):
    def test(self):
        print("test 运行")

f = FunctionTester()
f.test()