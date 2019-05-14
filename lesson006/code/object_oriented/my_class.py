# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 20:55
# @Author  : zdRan
# @FileName: my_class.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

"""

python 命名规范 驼峰命名
其他 全部小写，以短下划线（_）连接
"""
def func():
    pass


class Person:

    def func1(self):
        pass

    name = "女娲"
    age = 10000

    __private_args = "类私有变量"

    # def __init__(self):
    #     print("构造函数运行")

    def __init__(self,name,age):
        print(name)
        print(age)

    def get_private_ars(self):
        return self.__private_args

    def __private_method(self):
        print("私有方法")

    def _protected_method(self):
        print("保护方法")
    # 类方法可以访问类的成员
    @classmethod
    def my_class_method(cls):
        print(cls.name)
        print("类方法")
    # 静态方法不能访问类的成员
    @staticmethod
    def my_static_method():
        print("静态方法")
p = Person("aa",123)

print(Person.__dict__)
print(Person._Person__private_args)
p._Person__private_method()