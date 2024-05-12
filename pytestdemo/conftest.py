import pytest


@pytest.fixture(scope="class")
def setup():
    print(" This is setup and it will execute first as it has fixture decorator")
    yield
    print(" I will execute in the last")


@pytest.fixture()
def sendData():
    print("Send the data to other ")
    return ["Sujeet", "Sharma", "LPU"]


@pytest.fixture(params=[("Chrome", "FireFox"), ("IE", "Safari"), "Brave"])
def crossBrowser(request):
    return request.param
