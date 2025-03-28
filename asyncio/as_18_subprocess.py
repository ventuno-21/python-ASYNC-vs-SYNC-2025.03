"""
subprocess

methods:
i) create_subprocess_exec
ii) create_subprocess_shell

"""

import asyncio


async def main():
    process = await asyncio.create_subprocess_exec("python", "-l")
    print(f"process id is : {process.pid}")
    status_code = await process.wait()
    print(f"status code = {status_code}")


asyncio.run(main())
