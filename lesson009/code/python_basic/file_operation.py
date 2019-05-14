# 文件操作
from typing import AnyStr


def read_file():
    # 文件名，权限(r、w)
    file = open("exception.py", "r", encoding="UTF-8")
    # print(file.read())# 一次性加载，文件过大占用内存
    print(file.read(10))
    file.close()


# read_file()

# with open
# func(形参:类型 = 默认值) -> 返回类型
# 非强制，解释说明
def read_file2(filename: str = "aaa") -> AnyStr:
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        print(lines)


# read_file2("exception.py")

def read_file3(filename: int = -1) -> "这是解释说明":
    print(filename)
    read_file3.__annotations__["info"] = "动态注释"
    print(read_file3.__annotations__)


read_file3()


def write_file():
    with open("1.txt", "w", encoding="utf-8") as f:
        for i in range(100):
            f.write(str(i))
            f.flush()  # 刷新缓冲区


write_file()
