import asyncio
import random


# async - функция асинхронна, т.е. исполняется с пом asyncio(или др.),
# функция использует awair-ы и она не блокирующая (нет input, sleep)
async def f():
    while True:
        print('f() function')
        await asyncio.sleep(1)


def g_helper():
    print('g_helper()')
    return random.randint(0, 100)


async def g():
    while True:
        # print('g() function')
        print(g_helper())
        # сон в asyncio - возвращает в main и ищет следующую задачу -
        # сигнал о том, что можно переключиться на другую задачу
        await asyncio.sleep(1)
        # print('g() completed')


async def main():
    # # не просто вызывает функцию, а создает подзадачу
    # # (сопрограмму), которая не блокирует исполнение
    # # ждем результата g
    # await g()

    # создает задачу main() и g() параллельно
    main_loop.create_task(g())
    await f()


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()
