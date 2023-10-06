import asyncio


# async def print1():
#     print(1)

# async def print2():
#     print(2)
#     await asyncio.sleep(0)
#     print('Stop')

# async def print3():
#     print(3)


# async def print1():
#     await asyncio.sleep(2)
#     print(1)

# async def print2():
#     await asyncio.sleep(0)
#     print(2)

# async def print3():
#     await asyncio.sleep(1)
#     print(3)

# async def print4():
#     print(4)


# async def loop1():
#     i = 0
#     while True:
#         await asyncio.sleep(1)
#         i += 1
#         print(i)

# async def loop2():
#     i = 0
#     while True:
#         await asyncio.sleep(1)
#         i += 1
#         print(i)

# async def loop3():
#     i = 0
#     while True:
#         await asyncio.sleep(1)
#         i += 1
#         print(i)


# async def print1(x):
#     await asyncio.sleep(0)
#     return x ** 2


# async def print2(x):
#     y = await print1(x)
#     print(y ** 2)


# async def main():
    # task1 = asyncio.create_task(print1())
    # task2 = asyncio.create_task(print2())
    # task3 = asyncio.create_task(print3())
    # await task1
    # await task2
    # await task3

    # tasks = (
    #     asyncio.create_task(print1()),
    #     asyncio.create_task(print2()),
    #     asyncio.create_task(print3())
    # )
    # await asyncio.gather(*tasks)

    # await asyncio.gather(
    #     asyncio.create_task(print1()),
    #     asyncio.create_task(print2()),
    #     asyncio.create_task(print3())
    # )

    # await asyncio.gather(
    #     asyncio.create_task(print1()),
    #     asyncio.create_task(print2()),
    #     asyncio.create_task(print3()),
    #     asyncio.create_task(print4())
    # )

    # await asyncio.gather(
    #     asyncio.create_task(loop1()),
    #     asyncio.create_task(loop2()),
    #     asyncio.create_task(loop3())
    # )

    # await asyncio.gather(
    #     asyncio.create_task(print2(2)),
    # )

# if __name__ == '__main__':
#     asyncio.run(main())


##########################################


# async def custom_coro():
#     await asyncio.sleep(1)
 

# coro = custom_coro()
# print(type(coro))


##########################################
# Дана первая функция:
async def foo(x):
    await asyncio.sleep(0)
    return x ** 2

# Дана вторая функция, которая зависит от первой:
async def bar(x):
    # Здесь необходимо получить значение из функции foo(x) и записать в переменную "y"
    # print(y ** 2)
    pass

# Сформировать правильную очередь задач

########################################################

async def main():

    await asyncio.gather(
        asyncio.create_task(bar(2))
    )

if __name__ == '__main__':
    asyncio.run(main())