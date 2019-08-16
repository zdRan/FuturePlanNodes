# 事件：线程间的通信

import threading, time


class Boss(threading.Thread):
    def run(self):
        print("Boss：开始996，欢呼吧")
        # 事件设置
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("Boss：算了，不996了")
        print(event.isSet())
        event.set()


class Worker(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print(self.name+"worker：run")
        event.wait()
        print(self.name+"Worker:坚决反对996！！")
        #event.clear()
        event.wait()
        print(self.name+"Worker:OK!!!!!")


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker(str(i)))

    threads.append(Boss())

    for t in threads:
        t.start()