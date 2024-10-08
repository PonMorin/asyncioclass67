# example of using an asyncio queue without blocking
from random import random
import asyncio
from time import time

# coroutine to generate work
async def producer(queue):
    start = time()
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = 0.8
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    end = time() - start
    print(f"ALL Producer done in {end} sec")
 
# coroutine to consume work
async def consumer(queue):
    start = time()
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
    end = time() - start
    print(f"ALL Consumer done in {end} sec")
 
# entry point coroutine
async def main():
    # create the shared queue
    start = time()
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end = time() - start
    print(f"All done in {end} sec")
 
# start the asyncio program
asyncio.run(main())