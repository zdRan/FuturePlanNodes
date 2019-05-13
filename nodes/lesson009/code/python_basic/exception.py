"""

BaseException 是所有异常类的基类
处理方式

try:
    代码块
except 异常名称
    代码块：处理异常
else:
    代码块，不抛出异常被执行
finally:
    总是会被执行
"""

# try:
#     file = open("aa", "r")
#     i = 1
# except FileNotFoundError as e:
#     print(e)
#     print("发现异常,没有找到文件")
# else:
#     print("没有发生异常")


# 子类异常在前，父类异常在后，
try:
    file = open("aa", "r")
    i = 1
except FileNotFoundError as e:
    print("发现异常,没有找到文件")
except Exception:
    print("发生异常")
else:
    print("没有发生异常")
finally:
    print("无论如何都会被执行")

# 手动抛出异常
raise Exception("手动抛出异常")

# 自定义异常
class MyDefineError(BaseException):
    pass

#raise MyDefineError("抛出自定义异常")


