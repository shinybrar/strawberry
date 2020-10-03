from asyncio.futures import Future
from typing import Callable, Generic, List, TypeVar


T = TypeVar("T")
K = TypeVar("K")


class Dataloader(Generic[T, K]):
    batch: List[Future] = []

    def __init__(self, load_fn: Callable):
        self.load_fn = load_fn

    # TODO: how can make future generic here?
    async def load(self, id: K) -> Future:
        # if we have an entry in our cache, we should return the
        # promise from there

        # TODO: pass loop?
        future: Future = Future()

        self.batch.append(future)

        return future
