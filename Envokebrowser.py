import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

print("Selenium Version you are using = ", selenium.__version__)

#driver = webdriver.Edge()
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
'''This is for when we have have offline chrome browser and chrome driver if vpn resrticted the driver access 
other wise we can user direct by using driver = webdriver.Chrome() driver.get("https://www.cricbuzz.com/")
'''
#s = Service("C:\Users\sujeet.sharma\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=s)

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

driver.find_element(By.CLASS_NAME, "cb-plus-ico").click()
print("--- Click for login icon done ---")
time.sleep(2)

driver.find_element(By.ID, "cb-plus-signup-option").click()
print("---Clicked on signup done---")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("sujeet.sharma+1@utradesolutions.com")
print("---Email id filled for signup---")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='eventbutton']").click()
print("---Clicked on continue done while filled the email during signup---")
time.sleep(2)

# Login on crickbuzz site

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("sujeet.sharma+1@utradesolutions.com")
print("--- Email id filled for login ---")
time.sleep(5)
