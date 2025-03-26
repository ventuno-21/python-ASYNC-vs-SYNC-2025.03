"""
Queue
"""

from time import time, perf_counter, sleep
from multiprocessing import Process, current_process, Queue
import os


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def info(title):
    print(f"{bcolors.WARNING}{title}{bcolors.ENDC}")
    print("module name:", __name__)
    print(f"parent process: {bcolors.OKBLUE}{os.getppid()}{bcolors.ENDC}")
    print(f"process id: {bcolors.OKBLUE}{os.getpid()}{bcolors.ENDC}")


numbers = []


def p1_func(queue):
    nums = queue.get()
    nums.extend([1, 2, 3])
    queue.put(nums)
    print(f"numbers inside p1_func = {nums}")


def p2_func(queue):
    nums = queue.get()
    nums.extend([4, 5, 6])
    queue.put(nums)
    print(f"numbers inside p2_func = {nums}")


def p3_func(queue):
    nums = queue.get()
    nums.extend([7, 8, 9])
    queue.put(nums)
    print(f"numbers inside p3_func = {nums}")


if __name__ == "__main__":
    main_start = perf_counter()

    info("main line")

    qs = Queue()

    qs.put(numbers)

    p1 = Process(target=p1_func, args=(qs,), name="First")
    p2 = Process(target=p2_func, args=(qs,), name="second")
    p3 = Process(target=p3_func, args=(qs,))

    p1.start()
    p2.start()
    p3.start()

    print(f"is alive = {p1.is_alive()}")
    print(f"is alive = {p2.is_alive()}")

    p1.join()
    p2.join()
    p3.join()

    print(f"how p1 is exited? {bcolors.OKGREEN}{p1.exitcode}{bcolors.ENDC}")
    print(f"how p2 is exited? {bcolors.OKGREEN}{p2.exitcode}{bcolors.ENDC}")
    print(f"Final numbers list = {qs.get()}")

    main_end = perf_counter()

    print(
        f"Time to complete whole process:{bcolors.OKGREEN} {round(main_end - main_start, 5)} seconds{bcolors.ENDC}"
    )
