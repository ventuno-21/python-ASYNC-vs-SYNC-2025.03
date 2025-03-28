"""
LOCK

in asyncio we only have one thread, but we can have many tasks

lock methods:
i) acquire
ii) release
3) locked => is boolean

"""

import asyncio

counter = 0


# # without context manager
# async def increment(lock):
#     global counter
#     await lock.acquire()
#     try:
#         temp_counter = counter
#         temp_counter += 1
#         await asyncio.sleep(1)
#         counter = temp_counter
#     finally:
#         lock.release()


# with context manager
async def increment(lock):
    global counter
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(1)
        counter = temp_counter


async def main():
    lock = asyncio.Lock()
    global counter
    tasks = [asyncio.create_task(increment(lock)) for _ in range(15)]
    await asyncio.gather(*tasks)
    print(f"counter is:  {counter}")


asyncio.run(main())
