# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 14:06
# @Author  : zdRan
# @FileName: func_param.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

# 关键字参数
def my_func1(name, age):
    print(name)
    print(age)
    pass

my_func1(1, 2)
my_func1(name="zhangsan", age=22)
my_func1(age=33,name="lisi")

# 默认参数

def my_func_2(name = "zhang",age = 11):
    print(name)
    print(age)
    pass

my_func_2(age=22)

def my_func_3(name,age = 11):
    print(name)
    print(age)
    pass

my_func_3("zz",33)

# 函数返回值
def my_func_4(x):
    return "参数为"+str(x)

print(my_func_4(3))


# 递归

def fun(x):
    if x == 1:
        return 1
    return x + fun(x-1)

r = fun(6)
print(r)