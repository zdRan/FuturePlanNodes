# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 9:52
# @Author  : zdRan
# @FileName: if.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

if True:
    print("True")

if False:
    print("False")

if 1:
    print("1")

if 2:
    print(2)
# 小于等于 0 的值为 false
if 0:
    print("0")
else:
    print("1")

# 绝对等于
a = [1,2,3]
b = a
c = [1,2,3]

if a== b:
    print("a == b")
if a == c:
    print("a == c")
if a is b:
    print("a is b")

if a is c:
    print("a is c")

# 字符串比较
if "a"> "b":
    print("a>b")
else:
    print("a<b")

if "ac" >"ab":
    print("ac > ab")
else:
    print("ac <ab")

# 逻辑运算符

print("a" in "ab")
print("a" not in "ab")

if 1 and 2 and 3:
    print("1,2,3")

print(1 and 0)
print(1 or 0)
print(not 0)
print(not False)

# 身份运算

print(a is b)
print(a is c)
print(a is not c)