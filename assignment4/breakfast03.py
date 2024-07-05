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
    print("eggs: frying...")    
    await asyncio.sleep(3)     # 2: pause, another tasks can be run
    print("eggs: ready")

async def toast_break():       # 1
    print("toastL prepare ingridients")
    sleep(1)
    print("toast: break")
    await asyncio.sleep(3)    # 2: pause, another tasks can be run

async def main():                     # 1
    start = time()
    coffee_task = asyncio.create_task(make_coffee())        # Create Task for coffee
    egg_task = asyncio.create_task(fry_eggs())              # Create Task for egg
    toast_task = asyncio.create_task(toast_break())         # Create Task for toast
    await coffee_task  
    await egg_task
    await toast_task
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main())         # run top-level function concurrently