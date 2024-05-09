import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_run_setup(self):
        print(" This will run after setup function as it is associated with fixture decorator 1 ")

    def test_run_setup1(self):
        print(" This will run after setup function as it is associated with fixture decorator 2")

    def test_run_setup2(self):
        print(" This will run after setup function as it is associated with fixture decorator 3")

    def test_run_setup3(self):
        print(" This will run after setup function as it is associated with fixture decorator 4")
