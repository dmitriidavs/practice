import time
import functools
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         sleepage = func(*args, **kwargs)
#         finish = time.time() - start
#         print(f'Actual runtime: {finish}')
#
#         rv_str = f'Absolute time slept: {sleepage}'
#
#         return rv_str
#
#     return wrapper
#
#
# def runner(func):
#     def wrapper(*args, **kwargs):
#         runtime = 0
#         abs_sleepage = 0
#         start = time.time()
#         while runtime < 15:
#             abs_sleepage += func(*args, **kwargs)
#             runtime = time.time() - start
#             print(f'ABS: {abs_sleepage}')
#             print(f'ACT: {runtime}')
#             print('*' * 50)
#
#     return wrapper
#
#
# @runner
# def action(sleepage: float):
#     time.sleep(sleepage)
#     return sleepage
#
#
# action(1.2)
# # print(sleepage_time)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ' ,'.join(args_repr + kwargs_repr)
        logger.debug(f'function {func.__name__} called with args {signature}')
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f'Exception raised in {func.__name__}. exception: {str(e)}')
            raise e

    return wrapper


@log
def sum(a, b):
    print(a + b)


sum(10, b=20)
