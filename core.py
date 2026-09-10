import functools
import time
from typing import Callable, Any


class PerformanceOptimizer:
    def __init__(self, cache_size: int = 128):
        self.cache_size = cache_size

    @staticmethod
    def memoize(func: Callable) -> Callable:
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (args, frozenset(kwargs.items()))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper


def batch_process(data: list, chunk_size: int = 1000):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def timer_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result
    return wrapper


def optimized_compute(items: list) -> list:
    @PerformanceOptimizer.memoize
    def expensive_calc(val: int) -> int:
        return sum(i * i for i in range(val))

    return [expensive_calc(i) for i in items]