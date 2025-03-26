"""
1) Race condition
    it occurred when two or more than two threads work on same resource, 
    for example 'num' is shared resource

2) Thread safe
    race condition will be solved with thread safe
    with 'lock' it will be safe

    lock mmethods:
    I) acquire
    II) release
    III) locked

3) Dead lock
    It happend when instead of relase we use acquire again 
    For avoiding this problem it recommended to use context manager 
    so it release thread without  needing to use 'relase' method:

    so instead of below code:
    
    def add():
        global num
        lock.acquire()
        for _ in range(100000):
            num += 1
        lock.release()
        
    use this one:

    def add():
        global num
        with lock:
            for _ in range(100000):
                num += 1

"""

from time import sleep, time, perf_counter
from threading import Thread, current_thread, enumerate, Lock
from concurrent.futures import ThreadPoolExecutor
import sys

main_start = perf_counter()


num = 0
lock = Lock()


# Thread safe it with context manager
def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1


# Thread safe it without context manager
def subtract():
    global num
    lock.acquire()
    for _ in range(100000):
        num -= 1
    lock.release()


t1 = Thread(target=add)
t2 = Thread(target=subtract)

# we have to start our threads
t1.start()
t2.start()

# we have to join them too, otherwise it doesnt work correctly and instead of running program after await, will finish it
t1.join()
t2.join()

main_end = perf_counter()

print(
    f"Time to complete whole program with multi-threading: {round(main_end - main_start, 5)} seconds"
)

print(f"num = {num}")
