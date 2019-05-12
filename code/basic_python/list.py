# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 10:31
# @Author  : zdRan
# @FileName: list.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

list1 = [1,2,3,4]
print(list1)
print(type(list1))

list2 = [1,2,3.1,'a','b',list1]

print(list2)

# 访问

print(list1[1])

print(list1[1:3])

print(list1[1:])
print(list1[-2:])

# 添加
list1.append('a')
list1 = list1 + ['c','d']
print(list1)

# 更新
list1[0] = 0
print(list1)

# 删除

del list1[-1]
print(list1)
