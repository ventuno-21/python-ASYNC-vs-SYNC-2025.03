"""
Event loop
"""

import asyncio
from datetime import datetime


async def one(name):
    await asyncio.sleep(3)
    print(f"Hello, {name}")


async def main():
    a = asyncio.create_task(one("Farboad"))
    b = asyncio.create_task(one("Alma"))

    await a
    await b


print(f" start on = {datetime.now()}")

# asyncio.run(main())


loop = asyncio.new_event_loop()

# instead of run() we can use event-loop to run the task
try:
    loop.run_until_complete(main())
finally:
    # you have to close an event-loop
    loop.close()

print(f" done on  = {datetime.now()}")
