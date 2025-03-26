"""
1) terminate()

2) kill()
is same as terminate(), but terminate() is more gentlly 
3) exitcode
=0   => No error
>0  => The process had an error, and exited with that code
<0  => The process was jilled with a 'signal' of  -1*exitcode
"""

from time import time, perf_counter, sleep
from multiprocessing import Process, current_process
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


def show(name):
    start = time()
    print(f"start name = {name}")
    print(f"current process: {bcolors.OKBLUE}{current_process()}{bcolors.ENDC}")
    sleep(3)
    print(f"end name = {name}")
    end = time()

    print(f"Time to complete task for name ={name}: {round(end - start, 5)} seconds")


if __name__ == "__main__":
    main_start = perf_counter()

    info("main line")

    p1 = Process(target=show, args=("one",), name="First")
    p2 = Process(target=show, args=("two",))
    p1.start()
    p2.start()

    print(f"is alive = {p1.is_alive()}")
    print(f"is alive = {p2.is_alive()}")

    p1.terminate()
    # p2.terminate()

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
