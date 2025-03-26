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

4) RLOCK
    when two or more 'lock' be call at same time like below whole code will be on lock:

    lock = Lock()

    def add():
        global num
        with lock:
            # one like is here, second lock is inside subtract:
            subtract()
            for _ in range(100000):
                num += 1
                
    threfore instead of Lock() we use RLOCK() and the problem will be solved:

    lock = RLock()

    def add():
        global num
        with lock:
            subtract()
            for _ in range(100000):
                num += 1
                    
                   
5) Semaphore

    Semaphore methods:
    I) acquire
    II) release

    example: 

    lock = Semaphore()

    def add():
        global num
        lock.acquire()
        print(f"current thread = {current_thread().getName()}")
        sleep(2)
        num += 1
        lock.release()
        
    we have 7 threads so it will take more than 14 seonds to run, to avoid this, you can use 'value',
    with value the thread can be run together:


    lock = Semaphore(value=7)

    def add():
        global num
        lock.acquire()
        print(f"current thread = {current_thread().getName()}")
        sleep(2)
        num += 1
        lock.release()

    The time to execute above code is about 2 seconds, because we use value
    
    You can use 'release' more than once so for avoiding this problem you can use => BoundSemaphore
    Below code with semaphore wont face any problem, 
    so its better to use boundedsemaphore to face an error when running this code:
    
    def add():
        global num
        lock.acquire()
        print(f"current thread = {current_thread().getName()}")
        sleep(2)
        num += 1
        lock.release()
        lock.release()
        lock.release()

6) BoundedSemaphore
    with bounded semaphore you are not able to put more than once release method:

    def add():
        global num
        lock.acquire()
        print(f"current thread = {current_thread().getName()}")
        sleep(2)
        num += 1
        lock.release()
        lock.release()
        lock.release()

    And above code will face a problem
"""

from time import sleep, time, perf_counter
from threading import (
    Thread,
    current_thread,
    enumerate,
    Lock,
    RLock,
    Semaphore,
    BoundedSemaphore,
)
from concurrent.futures import ThreadPoolExecutor

main_start = perf_counter()


num = 0
lock = BoundedSemaphore(value=7)


# def add():
#     global num
#     lock.acquire()
#     print(f"current thread = {current_thread().getName()}")
#     sleep(2)
#     num += 1
#     lock.release()


# above code with context manager
def add():
    global num
    with lock:
        print(f"current thread = {current_thread().getName()}")
        sleep(2)
        num += 1


t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)
t7 = Thread(target=add)

# we have to start our threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

# we have to join them too, otherwise it doesnt work correctly and instead of running program after await, will finish it
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()

main_end = perf_counter()

print(
    f"Time to complete whole program with multi-threading: {round(main_end - main_start, 5)} seconds"
)

print(f"num = {num}")
