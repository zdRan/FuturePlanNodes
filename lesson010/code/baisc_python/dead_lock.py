import time
from threading import Thread, currentThread, RLock

# 递归锁 ，不能互斥
#mutexA = mutexB = RLock()

# 互斥锁
mutexA = RLock()
mutexB = RLock()

class House(Thread):
    def run(self):
        self.room1()
        self.room2()

    def room1(self):
        mutexA.acquire()
        print(currentThread().name + " 房间 1 拿到 A 锁")
        mutexB.acquire()
        print(currentThread().name + " 房间 1 拿到 B 锁")
        mutexB.release()
        print(currentThread().name + "房间 1 释放 B 锁")
        mutexA.release()
        print(currentThread().name + "房间 1 释放 A 锁")

    def room2(self):
        mutexB.acquire()
        print(currentThread().name + " 房间 2 拿到 B 锁")
        time.sleep(1)
        mutexA.acquire()
        print(currentThread().name + " 房间 2 拿到 A 锁")
        mutexA.release()
        print(currentThread().name + " 房间2 释放 A 锁")
        mutexB.release()
        print(currentThread().name + "房间 2 释放 B 锁")


if __name__ == "__main__":
    for i in range(10):
        t = House()
        t.start()
