from asyncio.events import get_event_loop

import pytest

from strawberry.dataloader import Dataloader


pytestmark = pytest.mark.asyncio


async def test_example():
    async def idx(keys):
        return keys

    loader = Dataloader(load_fn=idx)

    print("awaiting")
    value = await loader.load(1)
    print("done awaiting")

    assert value == 1
