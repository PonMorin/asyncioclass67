# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():       # 1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)      # 2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():          # 1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")    # 2: pause, another tasks can be run
    await asyncio.sleep(3)
    print("eggs: ready")

async def main():                     # 1
    start = time()
    coro = [make_coffee(), fry_eggs()]
    await asyncio.gather(*coro)
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main())         # run top-level function concurrently