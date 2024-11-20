#! /usr/bin/python3

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开启线程", self.name)
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        threadLock.release()

def print_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (name, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = myThread(1, 'Thread-1', 10)
thread2 = myThread(2, 'Thread-2', 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("退出主线程")