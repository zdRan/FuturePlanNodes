# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 14:36
# @Author  : zdRan
# @FileName: func_return.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

def func1():
    print("函数调用")


def func2():
    return "a"


f = func1()
f = func2()
print(f)
print(type(f))


def func3(x, y):
    return x + y


f = func3(1, 3)
print(f)
print(type(f))


# 多个返回值
def func4():
    return 3, 4


x, y = func4()
print(x)
print(y)


# 返回一个函数
def func5(x):
    if x == 2:
        def inner_func(y):
            print("inner 1被调用")
            return y * y
    if x == 3:
        def inner_func(y):
            print("inner 1被调用")
            return y * y * y

    return inner_func


calc = func5(2)
print(type(calc))
z = calc(4)
print(z)
