from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Dict, List


class TaskExecutor:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._cache: Dict[str, Any] = {}

    def _get_cache_key(self, func: Callable, args: tuple, kwargs: dict) -> str:
        key_data = (func.__name__, args, tuple(sorted(kwargs.items())))
        return str(hash(key_data))

    def execute_cached(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        key = self._get_cache_key(func, args, kwargs)
        if key not in self._cache:
            self._cache[key] = func(*args, **kwargs)
        return self._cache[key]

    def map_parallel(self, func: Callable, items: List[Any]) -> List[Any]:
        if not items:
            return []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(func, items))

    def batch_process(
        self, func: Callable, items: List[Any], batch_size: int = 50
    ) -> List[Any]:
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i : i + batch_size]
            results.extend(self.map_parallel(func, batch))
        return results

    def clear_cache(self) -> None:
        self._cache.clear()
