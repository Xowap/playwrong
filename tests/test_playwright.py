import asyncio
import pytest


def get_true():
    return True


async def a_get_true():
    return get_true()


@pytest.mark.playwright
def test_pw_true(playwright):
    ...


def test_true():
    assert get_true()


def test_a_true():
    assert asyncio.run(a_get_true())


@pytest.mark.asyncio
async def test_pa_true():
    assert await a_get_true()
