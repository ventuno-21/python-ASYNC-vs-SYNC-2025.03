"""
shield, => avaoid task to be cancelled
it will protect an awaitable object form get cancelled

timeoutError

"""

import asyncio
from asyncio import TimeoutError


async def one():
    await asyncio.sleep(6)
    print("hello")


async def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(asyncio.shield(a), timeout=5)
    except TimeoutError:
        print("Task is taking more time than usual, please be patient ...")
        await a

    print(f"Is the task cancelled? {a.cancelled()}")


asyncio.run(main())
