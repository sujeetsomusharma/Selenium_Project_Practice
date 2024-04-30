from selenium import webdriver
import time
# chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

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

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#  //a[contains(@href,'shop')]    a[href*='shop']   --> regular expression syntax for CSS_Selector and XPATH
driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5)
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 20)

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
time.sleep(5)
driver.find_element(By.LINK_TEXT, "India").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(5)
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
time.sleep(5)
assert "Success! Thank you!" in successText
driver.close()
