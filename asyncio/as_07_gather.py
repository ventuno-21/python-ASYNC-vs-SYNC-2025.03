"""
1) aiohttp 
    its a library that looks like requests library but it works asyncrounously

2) gather
    for avaoiding to write too many create_task, we can use gather
"""

import aiohttp
import asyncio


async def show_status(session, url):
    async with session.get(url) as response:

        print("Status:", response.status)
        print("Content-type:", response.headers["content-type"])

        html = await response.text()
        print("================================")
        print("fist 25 charachters of Body:", html[:25], "...")
        print("================================")
        return response.status


async def main():

    async with aiohttp.ClientSession() as session:
        urls = [
            "http://python.org",
            "https://pypi.org/project/aiohttp/",
            "https://github.com/ventuno-21",
        ]

        reqs = [show_status(session, url) for url in urls]
        # "*" will open a list
        status_codes = await asyncio.gather(*reqs, return_exceptions=True)

        print(f"status_codes are ====== {status_codes}")


asyncio.run(main())
