# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 12:13
# @Author  : zdRan
# @FileName: function_args.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
"""

函数的参数：

函数参数
对象参数
必须参数、默认参数、组合参数
**kwargs：关键字参数
*args：可变参数
"""


def function_demo1(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))


function_demo1(1, 2, 3, 4, name="zhangsan", age=12)

# 命名参数： * 后面的参数必须写名字，必须传递，如果不需要传，必须给默认值
def function_demo2(a,b,*,c,d):
    print(a,b,c,d)


function_demo2(1,2, c = 3,d = 4)

# 元组传参

def function_demo4(a,b,c):
    print(a,b,c)

# 元组拆分
s = (1,3,4)
function_demo4(*s)
# 集合拆分
s1 = [4,5,6]
function_demo4(*s1)
# 字典拆分
kw = {"a":1,"b":2,"c":3}
# 只传递 key
function_demo4(*kw)
# 传递value，字典的 key 必须要和函数的名称对应
function_demo4(**kw)