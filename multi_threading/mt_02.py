from time import sleep, time, perf_counter
from threading import Thread

main_start = perf_counter()


def show(name, delay):
    start = time()
    print(f"start name = {name}")
    sleep(delay)
    print(f"end name = {name}")
    end = time()

    print(f"Time to complete task for name ={name}: {round(end - start, 5)} seconds")


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


t1 = ShowThread("one", 2)
t2 = ShowThread("two", 5)

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
