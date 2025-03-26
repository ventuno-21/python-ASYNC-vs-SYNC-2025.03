"""
TimeoutError, wait_for()

"""

import asyncio
from asyncio import TimeoutError


async def one():
    await asyncio.sleep(6)
    print("hello")


async def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(a, timeout=5)
    except TimeoutError:
        print("You passed your deadline ...")

    print(f"Is the task cancelled? {a.cancelled()}")


asyncio.run(main())
