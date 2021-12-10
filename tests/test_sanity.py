import pytest


def test_sanity_pass() -> None:
    assert 1 == 1


@pytest.mark.xfail
def test_sanity_fails() -> None:
    x = 0
    y = 1
    assert x == y
