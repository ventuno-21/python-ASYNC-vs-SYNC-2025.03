"""
wait(return_when=FIRST_COMPLETED)

    return two sets of Tasks/Futures: (done, pending)
    
    return_when:
        indicates when this function should return, it must be one of the following:
        i) FIRST_COMPLETED
        ii) FIRST_EXCEPTION
        iii) ALL_COMPLETED
 
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

    status_codes = []

    async with aiohttp.ClientSession() as session:
        urls = [
            "http://python.orgdd",
            "https://pypi.org/project/aiohttp/",
            "https://github.com/ventuno-21",
        ]

        # requests = [show_status(session, url, 3) for url in urls]
        requests = [
            asyncio.create_task(show_status(session, urls[0])),
            asyncio.create_task(show_status(session, urls[1])),
            asyncio.create_task(show_status(session, urls[2])),
        ]

        done, pending = await asyncio.wait(
            requests, return_when=asyncio.FIRST_COMPLETED
        )
        print(f"done => {done} \npending =>{pending}")

        for d in done:
            print(await d)

        # # instead of "gather" we can use as_completed
        # for rqs in asyncio.as_completed(requests):
        #     status_codes = await rqs

        # # "*" will open a list
        # # status_codes = await asyncio.gather(*requests, return_exceptions=True)

        # print(f"status_codes are ====== {status_codes}")


asyncio.run(main())
