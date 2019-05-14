# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 13:43
# @Author  : zdRan
# @FileName: tuple.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

t = ("1")
t = (1)
print(type(t))
t = (1,)
print(type(t))

t = (1, 3, 4, 5, 6)
print(t[0])

# 元组中的 l 是指针类型，指针不可变，指针的实际地址内容可变
l = ["a", "b", "c"]
t = (1, 2, 3, l)
l.append("d")
print(t)
