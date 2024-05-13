import pytest


def test_creditNumber1():
    a = 4
    b = 6
    assert a + b == 10, "Credit card number is correct"


@pytest.mark.skip
def test_creditNumber2():
    a = 4
    b = 6
    assert a + b == 12, "Credit card number is not correct"


@pytest.mark.xfail(reason="This is a failed case which is not expected as per requirement")
def test_fail_case():
    print("Failed Case")


def test_load_browser(crossBrowser):
    print(crossBrowser)
