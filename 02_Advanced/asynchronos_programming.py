# Sample Code 00
# Welcome to our Python playground!

import asyncio
import time


# Here we fake the download of a large file by sleeping 1 second.
async def download_large_file(file_name):
    await asyncio.sleep(1)
    print(f"{file_name} was downloaded successfully")
    return f"{file_name}: OK"


# These are the files to download. Since each file takes 1 second
# to download, it would take 5 seconds without using asyncio.
FILES_TO_DOWNLOAD = [
    "textures.zip",
    "models.zip",
    "physics_engine.exe",
    "game.exe",
    "achievements.exe",
]


async def main():
    start_time = time.time()
    downloads = [download_large_file(file_name) for file_name in FILES_TO_DOWNLOAD]
    download_statuses = await asyncio.gather(*downloads)
    total_time = time.time() - start_time
    print(f"Finished downloading {len(download_statuses)} files in {total_time} seconds!")


# asyncio.run(main())

# Sample Code 01
import asyncio

async def print_something():
    await asyncio.sleep(1)
    print("something")
    return "finished"

async def main():
    print("main")
    # await print_something()
    task = asyncio.create_task(print_something())
    print("main again")
    result = await task
    print(result)

# print(type(main))
# print(type(main()))
# asyncio.run(main())

# Sample Code 02
async def print_values(values, delay):
    for item in values:
        print(item)
        await asyncio.sleep(delay)


async def main():
    # await print_values([1,3,5], 0.2)
    # await print_values([2,4], 0.3)

    task1 = asyncio.create_task(print_values([1,3,5], 0.2))
    task2 = asyncio.create_task(print_values([2,4], 0.3))

    await task1
    await task2

# asyncio.run(main())

# Sample Code 02
async def print_values(values, delay):
    for item in values:
        print(item)
        await asyncio.sleep(delay)

    return delay


async def main():
    values = await asyncio.gather(print_values([1,3,5], 0.2), print_values([2,4], 0.3) )

    print(values)

# asyncio.run(main())

# Sample Code 03
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    print("Done fetching")
    return [1,2,3,4,5,6]


async def run_algorithm():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    # data = await asyncio.gather(fetch_data(), run_algorithm())
    data = await asyncio.create_task(fetch_data())
    await run_algorithm()
    print(data)


# asyncio.run(main())

# Sample Code 04
import asyncio

async def gen(n):
    for i in range(n):
        yield i
        await asyncio.sleep(0.5)

async def main():
    async for i in gen(10):
        print(i)

# asyncio.run(main())

# Sample code 05
import asyncio

class Test:
    @staticmethod
    async def test():
        print("hi")

async def main():
    await Test.test()

asyncio.run(main())
