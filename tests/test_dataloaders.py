import asyncio

from strawberry.dataloader import Dataloader


def test_dataloaders(mocker):
    mock_batch_func = mocker.Mock()

    loader = Dataloader(mock_batch_func)

    async def a():
        await loader.load("1")

    async def b():
        await loader.load("2")

    async def run():
        await asyncio.gather(a(), b())

    asyncio.run(run())

    mock_batch_func.assert_called_once_with("a")
