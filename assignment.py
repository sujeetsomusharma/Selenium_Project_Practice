# Assignment ->
# 1- To validate the discounted price is less than the actual amount of the item
# 2 - To grab the product name and check with the expected list of items to the actual list of the items.


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

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print("The list are = ", results)

for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

if expected_list == actual_list:
    print("The actual and expected list are same")
else:
    print("The list in actual and expected are different")

print("All items are added to cart with 'ber' keyword items")

print("Add to cart now after product selection")
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
print("Click on cart is done")

print("Proceed to checkout")
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
print("Proceed to checkout Done")

promo_code = "rahulshettyacademy"
empty_promo_code = ''
wrong_promo_code = "ahulshettyacademy"

print("Add Promo Code")

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(promo_code)

print("Promo Code is Filled ... !")
print("Now Click on Add button to avail the discount")

driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
print("Click on Add button is Done")

wait_explicitly = WebDriverWait(driver, 10)
wait_explicitly.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
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

print("Print the sum of the items price")
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

sum_of_price = 0
for price in prices:
    sum_of_price = sum_of_price + int(price.text)
print(sum_of_price)

final_amount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
print("The final amount of the items is = ₹", final_amount)
print("Grab the discounted price and check whether it is less than the actual price")

discounted_price = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print("The discounted_price = ", discounted_price)

if discounted_price < final_amount:
    print("Discount Promo Code is applied !!!")
else:
    print("Discounted Promo Code is Invalid and not Applied")

print("---EOC---")
time.sleep(5)
