"""
Coroutine

* run() methods doesnt execute codes asyncrounously
async def one(name):
    await asyncio.sleep(3)
    print(f"Hello, {name}")
    
    
asyncio.run(one("Alma"))


threfore we use create_task() inside some function like main() as below:

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
# print(type(one("21")))
# asyncio.run(one("Alma"))
asyncio.run(main())

print(f" done on  = {datetime.now()}")
