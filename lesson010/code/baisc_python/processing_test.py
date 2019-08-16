import os
from threading import Thread

from multiprocessing import Process


def work():
    print(os.getpid())


if __name__ == "__main__":
    # 主进程启动的线程 PID 都等于 主线程的PID
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()

    print("主进程---> 线程 PID", os.getpid())
    # 线程 PID 不一样
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
