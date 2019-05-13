"""
lambda 表达式，
格式： lambda 参数列表： 表达式

"""


def f(x):
    return x + x


la = lambda x: x + x
print(la(2))

# map 函数
# 迭代 第二个参数，并传入到 第一个函数中，返回函数的结果
map_demo = map(la, [1, 2, 3, 4])
print(map_demo)
print(list(map_demo))
print(list(map(str, [1, 2, 3, 4])))

# reduce 函数
from functools import reduce

# 将前一个元素的函数结果，作为第二次迭代的参数传入函数,第三个参数为初始化参数，默认为空
r = reduce(lambda x, y: x + y, [1, 2, 3, 4], 10)
print(r)

# filter 函数
# 依次迭代 集合，过滤掉不符合函数的元素
print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8])))
print(list(filter(lambda x: x and x.strip(), [ "1", "aa", " ", None])))

