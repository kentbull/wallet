import pytest

from main import launcher
from wallet.core.configing import WalletConfig


@pytest.mark.asyncio
async def test_main_starts():
    # TODO change this test to send a shutdown signal to validate that the app starts and stops
    await launcher(WalletConfig())
    assert True
