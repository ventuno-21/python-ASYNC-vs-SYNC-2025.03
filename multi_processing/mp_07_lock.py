"""
Lock

Lock methods:
i) acquire
ii) release

"""

from time import time, perf_counter, sleep
from multiprocessing import Process, current_process, Lock
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


num = 0
lock = Lock()


def p1_func(num, lock):
    lock.acquire()
    for _ in range(100000):
        num += 1
    lock.release()


# use Lock with context manager
def p2_func(num, lock):
    with lock:
        for _ in range(100000):
            num -= 1


if __name__ == "__main__":
    main_start = perf_counter()

    info("main line")

    p1 = Process(target=p1_func, args=(num, lock), name="First")
    p2 = Process(target=p2_func, args=(num, lock), name="second")

    p1.start()
    p2.start()

    print(f"is alive = {p1.is_alive()}")
    print(f"is alive = {p2.is_alive()}")

    p1.join()
    p2.join()

    print(f"how p1 is exited? {bcolors.OKGREEN}{p1.exitcode}{bcolors.ENDC}")
    print(f"how p2 is exited? {bcolors.OKGREEN}{p2.exitcode}{bcolors.ENDC}")

    main_end = perf_counter()

    print(
        f"Time to complete whole process:{bcolors.OKGREEN} {round(main_end - main_start, 5)} seconds{bcolors.ENDC}"
    )

    print(f"Final amount of num is = {num}")
