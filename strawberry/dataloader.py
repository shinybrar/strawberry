from asyncio import create_task, get_event_loop
from asyncio.futures import Future
from typing import Awaitable, Callable, Generic, List, TypeVar


T = TypeVar("T")
K = TypeVar("K")


class Dataloader(Generic[T, K]):
    batch: List[Future] = []

    def __init__(self, load_fn: Callable):
        self.load_fn = load_fn

        self.loop = get_event_loop()

    def load(self, id: K) -> Awaitable:
        future = self.loop.create_future()

        async def dispatch():
            future.set_result("LOL")
            print("marked as done I guess")

        print("calling soon")

        self.loop.call_soon(create_task, dispatch())

        return future
