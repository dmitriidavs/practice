import time


# def func(f):
#     def wrapper(*args, **kwargs):
#         print('--- Start ---')
#         val = f(*args, **kwargs)
#         print('--- Finish ---')
#         return val
#
#     return wrapper
#
#
# @func
# def get_sum(x, y):
#     print('Func2 activated')
#     return x + y
#
#
# s = get_sum(2, 6)
# print(s)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        finish = time.time() - start
        print(f'Time: {finish}')

        return rv

    return wrapper


@timer
def test_func():
    for _ in range(10):
        time.sleep(0.01)


test_func()

# usecases: таймер, валидация входных данных, логирование
