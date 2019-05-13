# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 11:07
# @Author  : zdRan
# @FileName: loop.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

list1 = [1,2,3,4,5]

for i in list1:
    print(i)

i = 1

while i<6:
    i = i+1
    print(i)

list2 = [1,4,5,6,8,2,3,9,7,10]
for i in range(len(list2)-1):
    for j in range(len(list2)-1-i):
        if list2[j] > list2[j+1]:
            list2[j] , list2[j+1] = list2[j+1],list2[j]

print(list2)