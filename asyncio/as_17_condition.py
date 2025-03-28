"""
condition

"""

import asyncio


async def do_work(condition):
    async with condition:
        print("Lock")
        await condition.wait()
        print("Event is executed ... ")
        await asyncio.sleep(1)
        print("work is done")


async def fire_event(condition):
    await asyncio.sleep(5)
    async with condition:
        print("Notify all tasks ...")
        condition.notify_all()
    print("Notification finished. ")


async def main():
    condition = asyncio.Condition()
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))


asyncio.run(main())
