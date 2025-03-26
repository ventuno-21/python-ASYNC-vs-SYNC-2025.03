from time import sleep, time, perf_counter


main_start = perf_counter()


def show(name):
    start = time()
    print(f"start name = {name}")
    sleep(3)
    print(f"end name = {name}")
    end = time()

    print(f"Time to complete this task: {round(end - start, 5)} seconds")


show("one")
show("two")


main_end = perf_counter()

print(
    f"Time to complete whole program syncronously: {round(main_end - main_start, 5)} seconds"
)
