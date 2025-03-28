"""
1) semaphore(value=1)
    we can mention how many task run toghether with 'value' attribute

2) BoundedSemaphore
    it avoid the problem that you use moe than once release() method
    and in this case will arise an error and wont run a program 
    
    Also you are able to use contet manager to aoid any problem or error
"""

import asyncio


async def show(smp):
    await smp.acquire()
    print("show method")
    await asyncio.sleep(2)
    smp.release()


async def main():
    smp = asyncio.BoundedSemaphore(3)

    # all 15 task will be run toghether
    # await asyncio.gather(*[show() for _ in range(15)])

    # only 3 task will be run at a same time
    await asyncio.gather(*[show(smp) for _ in range(15)])


asyncio.run(main())
