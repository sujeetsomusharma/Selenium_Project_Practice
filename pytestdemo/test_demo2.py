import pytest


def test_nameFile1():
    print("Hi Sujeet")


@pytest.mark.smoke
def test_nameFile2():
    print("test_demo2.py")