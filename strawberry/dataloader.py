from asyncio.futures import Future
from typing import Any, Callable


class Dataloader:
    def __init__(self, load_fn: Callable):
        self.load_fn = load_fn

    async def load(self, id: Any) -> Future:
        ...
