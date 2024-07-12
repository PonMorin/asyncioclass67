from random import random
import asyncio


async def cooking_task(task, arg):
    print(f'Microwave ({task}): Cooking {arg} seconds...')
    await asyncio.sleep(arg)
    print(f'Microwave ({task}): Finished cooking')
    return f'{task} is completed in {arg}'

# main coroutine
async def main():
    # create many tasks
    cook_task = ['Rice', 'Noodle', 'Curry']
    tasks = [asyncio.create_task(cooking_task(task, 1 + random())) for task in cook_task]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report result
    print(f'Completed task: {len(done)}')
    print(f'- {done.pop().result()}')
    print(f'Uncompleted tasK: {len(pending)}')
    

# start the asyncio program
asyncio.run(main())