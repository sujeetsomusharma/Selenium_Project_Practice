import pytest


@pytest.fixture(scope="class")
def setup():
    print(" This is setup and it will execute first as it has fixture decorator")
    yield
    print(" I will execute in the last")