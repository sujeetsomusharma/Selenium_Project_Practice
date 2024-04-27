import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.select import Select

print("Selenium Version you are using = ", selenium.__version__)

# driver = webdriver.Edge()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
'''This is for when we have have offline chrome browser and chrome driver if vpn resrticted the driver access 
other wise we can user direct by using driver = webdriver.Chrome() driver.get("https://www.cricbuzz.com/")
'''
# s = Service("C:\Users\sujeet.sharma\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=s)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print("---Browser is open---")
time.sleep(2)

driver.maximize_window()
print("---Window maximize---")
time.sleep(2)

print("---The Title of the page is---")
print("The tile is = ", driver.title)
time.sleep(2)

print("---The url of the page is--- ")
print("The url of the page is = ", driver.current_url)
time.sleep(2)

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
time.sleep(5)

# loop to iterate the countries from the suggested list which is combination of "ind"

for country in countries:
    if country.text == "India":
        country.click()
        break

print("Country selected form dropdown is =  ", driver.find_element(By.ID, "autosuggest").get_attribute("value"))
time.sleep(5)
assert driver.find_element(By.ID, "auto-suggest").get_attribute( "value") == "India"  # this is for when we do not
# nned to print the output as on line number 49
time.sleep(2)
print("Correct Values is selected")

print(driver.find_element(By.XPATH, "//label[@for='ctl00_mainContent_chk_friendsandfamily']").text)
