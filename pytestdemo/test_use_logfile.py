import logging

import pytest

from pytestdemo.test_log_using_class import LogClass


@pytest.mark.smoke
class AddNumber(LogClass):

    def test_add_numbers(self, a, b):
        log = self.getLogger()
        log.info(a + b)
        return a + b


addNumber = AddNumber()
result = addNumber.test_add_numbers(4, 10)
print(f"The sum of 4 and 10 is {result}")
