"""
aiohttp =>
Asynchronous HTTP client/server for asyncio & python
its a library that looks like requests library but it works asyncrounously
"""

import aiohttp
import asyncio
import time

start = time.time()


async def send_pokemon(session, url, number):
    async with session.get(url) as response:
        # pokemon = response.json()
        pokemon = await response.json()
        print("===========================================")
        print(
            f"pokeman no.: {number} \tname: {pokemon["name"]} \tstatus code:{response.status}"
        )
        # print("Content-type:", response.headers["content-type"])
        # html = await response.text()
        # print("fist 100 charachters of Body:", html[:100], "...")


async def main():

    async with aiohttp.ClientSession() as session:
        for number in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            status = await send_pokemon(session, url, number)


asyncio.run(main())

print(f"Total time: {time.time()-start}")
