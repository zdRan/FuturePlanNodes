import threading
import time
import random

num = 1000


def my_print(info, info2):
    time.sleep(random.randint(1, 10))
    print("执行事件" + info + ":" + info2)
    # 全局变量，多线程共享
    global num
    num = num - 1
    print(num)


if __name__ == "__main__":
    # args 参数类型是一个元组
    t1 = threading.Thread(target=my_print, args=("线程1", "附加参数"))
    t2 = threading.Thread(target=my_print, args=("线程2", "附加参数"))
    t3 = threading.Thread(target=my_print, args=("线程3", "附加参数"))
    t4 = threading.Thread(target=my_print, args=("线程4", "附加参数"))
    t5 = threading.Thread(target=my_print, args=("线程5", "附加参数"))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    print("do something")
