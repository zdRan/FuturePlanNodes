# yield 生成器

def demo1():
    l = [x for x in range(100)]
    return l

a = demo1()

def yield_demo2():
    for x in range(10):
        yield x
        print("生成器")
    print("生成器外层")

a = yield_demo2()
print(a)

# for i in a:
#     print(i)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# 多生成器
def yield_demo2():
    a = 10
    b = 20
    c = 30
    for i in range(4):
        yield a
        print("a之后")
        yield b
        print("b 之后")
        yield c
        print("c 之后")

g = yield_demo2()

# for i in g:
#     print(i)


print(g.__next__())
print(g.__next__())
print(g.__next__())