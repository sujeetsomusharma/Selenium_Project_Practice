# n Selenium with Python, you can use explicit waits to wait for a certain condition to occur before proceeding
# further in the code. Explicit waits allow you to wait for a certain condition to occur before proceeding to the
# next step in the code execution. The WebDriverWait class takes the driver instance and the maximum amount of time to
# wait as parameters. The until method is used to wait until a specified condition becomes True.
#
# The expected_conditions module provides a variety of built-in conditions to wait for,
# such as element_to_be_clickable, visibility_of_element_located, text_to_be_present_in_element, and more. You can
# use these conditions according to your specific needs.
# Remember to replace "path_to_chromedriver" with the actual path to your ChromeDriver executable.

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

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(5)  # this sleep time is given because we are waiting for the
# list to return the values of list rest things is handles with time with implicitly_wait time

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # it will return list
print("Length of the product list with 'ber' suggested keyword", len(results))

product_names = []  # Initialize an empty list

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    # Assuming the product name is in a specific child element, like a <h4> or <p> tag
    product_name = result.find_element(By.CLASS_NAME, "product-name").text  # this is chaining method as find the
    # elements on "result" Replace 'product-name' with the actual
    # class or tag
    product_names.append(product_name)  # Add the product name to the list

print("Product Names:", product_names)

if len(product_names) >= len(results):
    print("Product are available to buy")
else:
    print("Products are not in stocks please select other times to buy if you wish to buy")

# click on Add Cart one by using chaining operation

for result in results:
    result.find_element(By.XPATH, "div/button").click()  # this is chaining method as in results all the product is
    # selected and by using this method we have used the single cart to select
print("All items are added to cart with 'ber' keyword items")

print("Add to cart now after product selection")
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
print("Click on cart is done")

print("Proceed to checkout")
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()  # //button[text()='PROCEED TO
# CHECKOUT']
# this type of find the text() is not available with the css selector.
print("Proceed to checkout Done")

promo_code = "rahulshettyacademy"
empty_promo_code = ''
wrong_promo_code = "ahulshettyacademy"

print("Add Promo Code")

# driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(promo_code)
# driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(empty_promo_code)
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(wrong_promo_code)

print("Promo Code is Filled ... !")
print("Now Click on Add button to avail the discount")

driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
print("Click on Add button is Done")

wait_explicitly = WebDriverWait(driver, 10)
wait_explicitly.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))  # this is
# used when the element presence is to identify. It will wait until the element is not appeared.
print("Explicit Code Applied")
promo_Info = driver.find_element(By.XPATH, "//div/span[@class='promoInfo']").text
print(promo_Info)

if promo_Info == "Code applied ..!":
    print(" --The promo code is applied --")
elif promo_Info == "Invalid code ..!":
    print(" -- The promo code is not a valid code --")
elif promo_Info == "Empty code ..!":
    print("-- No promo code is applied ---")
else:
    print(" ---No promo code option is available ---")

time.sleep(2)

print("EOC")
