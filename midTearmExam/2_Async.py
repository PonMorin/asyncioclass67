import asyncio

async def fibonacci(n):
    await asyncio.sleep(1)
    a, b = 0, 1

    if n <= 1:
        return n
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

async def main():
    n = 10
    coros = [asyncio.create_task(fibonacci(i)) for i in range(n)]
    # results = await asyncio.gather(*coros)
    # print(results)
    
    done, pending = await asyncio.wait(coros, return_when="ALL_COMPLETED")
    print(type(done))
    result_list = []
    for i in done:
        result_list.append(i.result())
    # result_list.sort()
    print(result_list)

asyncio.run(main())