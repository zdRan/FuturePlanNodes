# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 11:11
# @Author  : zdRan
# @FileName: decorator.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

"""
装饰器（语法糖、注解）

python 中装饰器不可以写多个，以第一个为准
"""

#
# def func_1(x):
#     return x * 2
#
#
# def func_2(x):
#     return x * 3
#
#
# def func_3(x, y, i, j):
#     return x(i) + y(j)
#
#
# r = func_3(func_1, func_2, 2, 3)
# print(r)
#

import time


def runtime_noargs(function_name):
    def wrapper():
        start_time = time.time()
        function_name()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


# 无参注解
@runtime_noargs
def func_demo1():
    print("demo1 函数运行::")


def runtime_args(function_name):
    def wrapper(args):
        if args > 10:
            print("参数错误：" + str(args))
        else:
            function_name(args)

    return wrapper


# 单个参数
@runtime_args
def func_demo2(args):
    print("demo1 函数运行::" + str(args))


func_demo2(2)


def many_args(function_name):
    def wrapper(*args):
        function_name(*args)

    return wrapper


@many_args
def function_demo3(*args):
    # args 元组类型
    print(type(args))
    print(*args)


# function_demo3("aaa", "bbb")
# key = value 参数

def dict_args(function_name):
    def wrapper(**kwargs):
        function_name(**kwargs)

    return wrapper


@dict_args
def function_demo4(**kwargs):
    # 字典类型
    print(type(kwargs))
    print(kwargs)


function_demo4(name="aaa", age=123)


# 组合类型参数
def comb_args(function_name):
    def wrapper(*args, **kwargs):
        function_name(*args, **kwargs)

    return wrapper


@comb_args
def function_demo5(*args, **kwargs):
    print(args)
    print(kwargs)


function_demo5(1, 2, name="qqqq", age=12)


# 装饰器参数
def decorator_args(timeout):
    def out_wrapper(function_name):
        def wrapper(*args, **kwargs):
            star = time.time()
            i = function_name(*args, **kwargs)
            end = time.time()
            user_time = end - star
            if user_time > timeout:
                print("运行超时")
            else:
                return i

        return wrapper

    return out_wrapper


@decorator_args(timeout=2)
def function_demo6(*args, **kwargs):
    time.sleep(3)
    print(args)
    print(kwargs)
    print("执行 function_demo6")


function_demo6(11,222)