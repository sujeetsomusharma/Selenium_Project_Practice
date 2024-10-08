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


# In Selenium for Python, select_by_value() is used to select an option from a dropdown list (which is created using
# the <select> tag) by specifying the value attribute of the <option> tag. This is done using the Select class from
# selenium.webdriver.support.ui.
# Here’s a step-by-step guide to using select_by_value():
# Steps:
# Import the required classes.
# Find the dropdown element (the <select> tag).
# Use the Select class to wrap the dropdown element.
# Call the select_by_value() method with the desired option's value.

# ----------Example--------------

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# # Initialize the driver
# driver = webdriver.Chrome()
#
# # Open the webpage with the dropdown
# driver.get('http://example.com')
#
# # Locate the dropdown element using its ID, name, or other attribute
# dropdown_element = driver.find_element_by_id('dropdown_id')
#
# # Wrap the element in a Select object
# select = Select(dropdown_element)
#
# # Select an option by its value attribute
# select.select_by_value('value_of_the_option')
#
# # Close the driver
# driver.quit()
# ------------------------------------------------------------------------------------------

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
assert driver.find_element(By.ID, "auto-suggest").get_attribute("value") == "India"  # this is for when we do not
# need to print the output as on line number 49
time.sleep(2)
print("Correct Values is selected")

print(driver.find_element(By.XPATH, "//label[@for='ctl00_mainContent_chk_friendsandfamily']").text)

driver.quit()
