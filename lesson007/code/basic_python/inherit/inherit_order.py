# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:40
# @Author  : zdRan
# @FileName: inherit_order.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

class A(object):
    def test(self):
        print("A类")

class B(A):
    def test1(self):
        print("B类")

class C(A):
    def test(self):
        print("C类")

class D(B):
    def test1(self):
        print("D类")

class E(C):
    def test(self):
        print("E类")

class F(D,E):
    pass

f = F()
f.test()

print(F.__mro__)