# example of running a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another coroutine
    await asyncio.sleep(1)

async def main():
    # execute my custom coroutine
    await custom_coro()

# create tbe coroutine
asyncio.run(main())