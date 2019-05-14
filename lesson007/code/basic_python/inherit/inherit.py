# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:10
# @Author  : zdRan
# @FileName: inherit.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

class Father():
    name = "李雷"
    sex = "男"

    # def __init__(self):
    #     print("Father构造函数调用")

    def speak_english(self):
        print("说英语")

    def __func(self):
        print("Father 的私有方法")


class Mother:
    name = "韩梅梅"
    sex = "女"

    def __init__(self):
        print("Mother 构造函数调用")

    def speak_chinese(self):
        print("说中文")


class Child(Father, Mother):
    # 如果不存在 构造函数 从左至右选择构造函数
    # def __init__(self):
    #     print("child 构造函数运行")

    def speak_english(self):
        print("child说英语")

    def study(self):
        print("child 学习")


child = Child()

child.speak_english()
child.speak_chinese()
print(Child.__bases__)
