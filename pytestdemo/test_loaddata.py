import pytest


@pytest.mark.usefixtures("sendData")
class TestLoadSetData:
    def test_load_data(self, sendData):
        print(sendData)
        print("The first item is the list is : ", sendData[0])
        print("The Second item is the list is : ", sendData[1])


@pytest.mark.usefixtures("crossBrowser")
class TestLoadBrowser:
    def test_browsers_loaded_correctly(self, crossBrowser):
        print("The Browsers are =", crossBrowser[1])
