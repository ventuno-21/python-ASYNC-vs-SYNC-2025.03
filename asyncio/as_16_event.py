"""
Event

i) wait()
ii) set()
iii) clear()
xi) is_set()
"""

import asyncio
import functools


def trigger_event(event):
    event.set()


async def do_work_on_event(event):
    print("waiting for an Event ...")
    await event.wait()
    print("Excuting my task...")
    await asyncio.sleep(5)
    print("Finished")
    event.clear()


async def main():
    event = asyncio.Event()
    asyncio.get_running_loop().call_later(3, functools.partial(trigger_event, event))
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))


asyncio.run(main())
