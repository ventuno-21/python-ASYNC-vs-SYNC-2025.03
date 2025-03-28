"""
1) semaphore(value=1)
    we can mention how many task run toghether with 'value' attribute

"""

import asyncio


async def show(smp):
    await smp.acquire()
    print("show method")
    await asyncio.sleep(2)
    smp.release()


async def main():
    smp = asyncio.Semaphore(3)

    # all 15 task will be run toghether
    # await asyncio.gather(*[show() for _ in range(15)])

    # only 3 task will be run at a same time
    await asyncio.gather(*[show(smp) for _ in range(15)])


asyncio.run(main())
