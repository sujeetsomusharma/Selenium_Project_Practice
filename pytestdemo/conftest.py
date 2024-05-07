import pytest


@pytest.fixture()
def setup():
    print(" This is setup and it will execute first as it has fixture decorator")
    yield
    print(" I will execute in the last")