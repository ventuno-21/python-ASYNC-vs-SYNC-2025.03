"""
1) Current-thread 
2) number of ALIVE threads in each process with 'enumerate'
as you can see its two thread in pur example but the number of alive threads is 3
one thread is the whole process which is mainthread
output:
Alive threads: [
    <_MainThread(MainThread, started 7912)>,
    <Thread(First, started 17036)>, 
    <Thread(second, initial)>
]      

"""

from time import sleep, time, perf_counter
from threading import Thread, current_thread, enumerate
import sys

main_start = perf_counter()


def show(name):
    start = time()
    print(f"current thread: {current_thread()}")
    print(f"Alive thread: {enumerate()}")
    print(f"start name = {name}")
    sleep(3)
    print(f"end name = {name}")
    end = time()

    print(f"Time to complete task for name ={name}: {round(end - start, 5)} seconds")


t1 = Thread(target=show, args=("One",), name="First")
t2 = Thread(target=show, args=("two",), name="second")

# we have to start our threads
t1.start()
t2.start()

# print(f"is t1 a daemon? {t1.isDaemon()}")
# print(f"is t2 a daemon? {t2.isDaemon()}")

# we have to join them too, otherwise it doesnt work correctly and instead of running program after await, will finish it
t1.join()
t2.join()

main_end = perf_counter()

print(
    f"Time to complete whole program with multi-threading: {round(main_end - main_start, 5)} seconds"
)

sys.exit()
