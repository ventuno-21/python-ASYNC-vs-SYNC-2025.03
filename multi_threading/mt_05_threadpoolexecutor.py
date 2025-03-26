"""
1) ThreadPoolExecutor
you can use max_worker, to finish like first 2 thread and 
then take another 2 and so on till be done,
otherwise all threads will be start toghether 
example: 

 with ThreadPoolExecutor(max_workers=2) as executor:
    names = ["one", "two", "three", "four", "five"]
    executor.map(show, names)
"""

from time import sleep, time, perf_counter
from threading import Thread, current_thread, enumerate
from concurrent.futures import ThreadPoolExecutor
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


with ThreadPoolExecutor() as executor:
    names = ["one", "two", "three", "four", "five"]
    executor.map(show, names)


main_end = perf_counter()

print(
    f"Time to complete whole program with multi-threading: {round(main_end - main_start, 5)} seconds"
)

# sys.exit()
