# Problem 4 --- TIM SOLUTIONS ---
import asyncio

async def add_one(coroutine):
    return_value = await coroutine()
    return return_value + 1

# Problem 5 --- TIM SOLUTIONS ---
import asyncio

async def append_two_values(lst, value1, value2):
    lst.append(value1)
    await asyncio.sleep(0.5)
    lst.append(value2)

lst = []

async def main(lst):
    futures = [append_two_values(lst, 1, 4), append_two_values(lst, 3, 6), append_two_values(lst, 2, 5)]
    await asyncio.gather(*futures)

asyncio.run(main(lst))
print(lst)
