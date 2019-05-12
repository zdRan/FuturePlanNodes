# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 13:10
# @Author  : zdRan
# @FileName: set.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

# 声明
set_param = set()
print(set_param)
print(type(set_param))

set_param = {1,2,3}
print(set_param)
print(type(set_param))

# in
print(1 in set_param)

# 集合运算
a = set("abcd")
b = set("cdef")

print(a | b)
print(a & b)

# 集合操作
my_set = set(("abc","cde","def"))

my_set.add("fgh")
print(my_set)

my_set.remove("abc")
print(my_set)
my_set.clear()
print(my_set)