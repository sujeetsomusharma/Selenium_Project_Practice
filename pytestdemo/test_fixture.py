import pytest


@pytest.fixture()
def setup():
    print(" This is setup and it will execute first as it has fixture decorator")
    yield
    print(" I will execute in the last")


def test_run_setup(setup):
    print(" This will run after setup function as it is associated with fixture decorator")
