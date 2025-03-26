from time import sleep, time, perf_counter
from threading import Thread

main_start = perf_counter()


def show(name):
    start = time()
    print(f"start name = {name}")
    sleep(3)
    print(f"end name = {name}")
    end = time()

    print(f"Time to complete task for name ={name}: {round(end - start, 5)} seconds")


t1 = Thread(target=show, args=("One",))
t2 = Thread(target=show, args=("two",))

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
