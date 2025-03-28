"""
aiohttp =>
Asynchronous HTTP client/server for asyncio & python
its a library that looks like requests library but it works asyncrounously
"""

import aiohttp
import asyncio


async def show_status(session, url):
    async with session.get(url) as response:

        print("Status:", response.status)
        print("Content-type:", response.headers["content-type"])

        html = await response.text()
        print("================================")
        print("fist 100 charachters of Body:", html[:100], "...")
        print("================================")
        return response.status


async def main():

    async with aiohttp.ClientSession() as session:
        url = "http://python.org"
        status = await show_status(session, url)

        print(f"status is ====== {status}")


asyncio.run(main())
