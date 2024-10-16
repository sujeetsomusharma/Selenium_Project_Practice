# Waits in selenium
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

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
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

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print("Length of the product list with 'ber' suggested keyword", len(results))

if len(results) > 5:
    print("Product are available to buy")
else:
    print("Products are not in stocks please select other times to buy if you wish to buy")

# click on Add Cart one by using chaining operation

for result in results:
    result.find_element(By.XPATH, "div/button").click()  # this is chaining method as in results all the product is
    # selected and by using this method we have used the single cart to select
print("All items are added to cart with 'ber' keyword items")
time.sleep(2)

print("Add to cart now after product selection")
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
print("Click on cart is done")

time.sleep(2)

print("Proceed to checkout")
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
print("Proceed to checkout Done")
time.sleep(2)

promo_code = "rahulshettyacademy"
empty_promo_code = ''
wrong_promo_code = "ahulshettyacademy"

print("Add Promo Code")

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(empty_promo_code)

print("Promo Code is Filled ... !")
print("Now Click on Add button to avail the discount")

driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
print("Click on Add button is Done")
time.sleep(10)

promo_Info = driver.find_element(By.XPATH, "//div/span[@class='promoInfo']").text
print(promo_Info)
time.sleep(5)

if promo_Info == "Code applied ..!":
    print(" --The promo code is applied --")
elif promo_Info == "Invalid code ..!":
    print(" -- The promo code is not a valid code --")
elif promo_Info == "Empty code ..!":
    print("-- No promo code is applied ---")
else:
    print(" ---No promo code option is available ---")

time.sleep(5)
