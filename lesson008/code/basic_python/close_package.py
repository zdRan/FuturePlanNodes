# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 22:19
# @Author  : zdRan
# @FileName: close_package.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

"""
闭包：外部函数的返回值是内部函数的引用
"""
def outer(a):
    b = 10
    def inner():
        print(a+b)
    # 外部函数的返回值，是内部函数的引用
    return inner

inner_func = outer(11)
print(inner_func)
inner_func()