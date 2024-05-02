# Any pytest file start with "test_"
# pytest method start with test only
# any coe should be wrapped in method only

def test_firstDemo():
    print("Hello")


def test_secondDemo():
    msg = "HI Good Morning"
    assert msg == "hi", "This is not the correct message"
