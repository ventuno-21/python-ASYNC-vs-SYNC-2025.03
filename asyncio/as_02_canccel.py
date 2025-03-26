"""
cancel, done, CancelledError Exception

"""

import asyncio
from asyncio import CancelledError


async def one():
    await asyncio.sleep(8)
    print("hello")


async def main():
    a = asyncio.create_task(one())

    seconds = 0

    while not a.done():
        print(f"Task is not finish ....")
        await asyncio.sleep(1)
        seconds += 1

        if seconds == 5:
            a.cancel()

    try:
        await a
    except CancelledError:
        print("Task is cancelled ...")


asyncio.run(main())
