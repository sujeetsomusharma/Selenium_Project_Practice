# Any pytest file start with "test_"
# pytest method start with test only
# any code should be wrapped in method only
# In pytest we can't have multiple test method name with the same and
# if it exists that means it will override the previous case.
# to run the scripts there are various method just like pytest.py -s -v -k
# -s is for logs in output, -k is to run specific methods using rgex, -v is for logs with more info with meta data,
# also we can run specifc file with file name like pytest.py "file name" -v -s -k.
# we can also run the specific method that we need to run smoke test with "@pytest.mark.smoke" with the flag name -m
# "@pytest.mark.skip" is to skip any method in pytest
# if any bug in any method but still want to run but with no output then we can use "@pytest.mark.xfail"

# In pytest, @pytest.mark is a decorator used for applying markers to tests and test functions. Markers are a way to
# add metadata or attributes to tests, allowing you to control how they are run or to categorize them for various
# purposes.

# You can use @pytest.mark to apply built-in markers provided by pytest or create your own custom markers. Here are
# some common uses:

# Built-in Markers:
# @pytest.mark.skip: Skips a test without running it.
# @pytest.mark.xfail: Marks a test as expected to fail.
# @pytest.mark.parametrize: Provides multiple sets of arguments to a test function.

import pytest

import pytestdemo


def test_firstDemo():
    print("Hello")


@pytest.mark.smoke
def test_secondDemo():
    msg = "Hi Good Morning"
    assert msg == "Hi Good Morning"
    # assert msg == "hi", "This is not the correct message"
