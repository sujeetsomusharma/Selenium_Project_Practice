import time

import driver
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

print("Selenium Version you are using = ", selenium.__version__)
# driver = webdriver.Edge()

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver = webdriver.Firefox()
'''This is for when we have have offline chrome browser and chrome driver if vpn resrticted the driver access 
other wise we can user direct by using driver = webdriver.Chrome() driver.get("https://www.cricbuzz.com/")
'''
# s = Service("C:\Users\sujeet.sharma\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=s)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print("---Browser is open---")

driver.maximize_window()
print("---Window maximize---")

print("---The Title of the page is---")
print("The tile is = ", driver.title)

print("---The url of the page is--- ")
print("The url of the page is = ", driver.current_url)

time.sleep(2)

print("Click on top deals of the website")
driver.find_element(By.LINK_TEXT, "Top Deals").click()
print("Click on top deal done")
time.sleep(2)

next_window_tab = driver.window_handles
print("Switch to next tab window after click on 'Top Deals'")
driver.switch_to.window(next_window_tab[1])

print("Next text on new tab = ", driver.find_element(By.XPATH, "//div/div[text()='GREEN']").text)
time.sleep(2)

print("The column which we need to sort is = ",
      driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").text)


list_of_items_before_click_on_Veg_fruit_name = driver.find_elements(By.XPATH, "//tr/td[1]")
list_of_items_before_click_on_Veg_fruit_name = [item.text for item in list_of_items_before_click_on_Veg_fruit_name]
print("The list of items before click = ", list_of_items_before_click_on_Veg_fruit_name)

time.sleep(2)

print("Click on the column to sort")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
time.sleep(2)

original_list_of_items = []

list_of_items = driver.find_elements(By.XPATH, "//tr/td[1]")    # list of items after click on Veg/fruit name
actual_list_of_items = [item.text for item in list_of_items]
print("The list is = ", actual_list_of_items)

for elements in list_of_items:
    original_list_of_items.append(elements.text)
browser_sorted_list = original_list_of_items.copy()

original_list_of_items.sort()

if original_list_of_items == browser_sorted_list:
    print("List is sorted")
    print("Sorted list is = ", browser_sorted_list)

else:
    print("List is not sorted")
    print("Unsorted list = ", actual_list_of_items)

time.sleep(5)
