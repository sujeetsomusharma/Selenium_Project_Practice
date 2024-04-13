import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

driver.get("https://www.cricbuzz.com/")
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

print("--- Click on Live Match")
driver.find_element(By.LINK_TEXT, "Live Scores").click()
time.sleep(5)

print("Click on Scheduled Matched on Cric-buzz")
driver.find_element(By.LINK_TEXT, "Schedule").click()
time.sleep(2)

print("--- Click on Archive tab on cric-buzz website---")
driver.find_element(By.CSS_SELECTOR,
                    "a[href='/cricket-scorecard-archives']").click()  # used css_selector without using // and @
time.sleep(2)

print("--- Click on News option of cric-buzz besides Archives ---")
driver.find_element(By.XPATH, "//div[@id='newsDropDown']").click()
time.sleep(5)

# static drop down code
print("Select the News option is clicked ")
driver.find_element(By.LINK_TEXT, "News").click()
print("All stories option is selected")
time.sleep(5)

print("Select the News option is clicked ")
driver.find_element(By.LINK_TEXT, "News").click()
print("All stories option is selected")
time.sleep(5)

print("Select the values form dropdown of news section")
driver.find_element(By.PARTIAL_LINK_TEXT, "Spotlight").click()
time.sleep(10)
print("Spotlight is selected")

print("---- END OF THE PAGE ----")
