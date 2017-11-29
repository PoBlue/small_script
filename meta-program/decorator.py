"""
Python CookBook: page 329
"""
import time
from functools import wraps


def timethis(func):
    """
    decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1


def main():
    countdown(100000)
    pass

if __name__ == '__main__':
    main()