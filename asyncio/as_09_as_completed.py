"""

1) aiohttp 
    its a library that looks like requests library but it works asyncrounously

2) gather
    for avaoiding to write too many create_task, we can use gather

3) as_completed
    When we receive an answer it will show it instantly
    
difference between gather() and as_completed():
    The gather method is used to run multiple tasks concurrently 
    and return the results as a list . 
    The as_completed returns a iterable is used to run multiple tasks concurrently 
    and return the results as they complete
    
"""

import aiohttp
import asyncio


async def show_status(session, url, delay):
    await asyncio.sleep(delay)

    async with session.get(url) as response:

        print("Status:", response.status)
        print("Content-type:", response.headers["content-type"])

        html = await response.text()
        print("================================")
        print("fist 25 charachters of Body:", html[:25], "...")
        print("================================")
        return response.status


async def main():

    status_codes = []

    async with aiohttp.ClientSession() as session:
        urls = [
            "http://python.org",
            "https://pypi.org/project/aiohttp/",
            "https://github.com/ventuno-21",
        ]

        # requests = [show_status(session, url, 3) for url in urls]
        requests = [
            show_status(session, urls[0], 9),
            show_status(session, urls[1], 6),
            show_status(session, urls[2], 3),
        ]

        # instead of "gather" we can use as_completed
        for rqs in asyncio.as_completed(requests):
            status_codes = await rqs

        # "*" will open a list
        # status_codes = await asyncio.gather(*requests, return_exceptions=True)

        print(f"status_codes are ====== {status_codes}")


asyncio.run(main())
