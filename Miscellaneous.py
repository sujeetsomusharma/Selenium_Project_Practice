import time

import document
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
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

print("Scroll up-to only 500px height")
driver.execute_script("window.scroll(0,500);")
time.sleep(5)

print("Scroll to the bottom of the page")
driver.execute_script("window.scroll(0,document.body.scrollHeight);")  # this "execute_script" is used to run the
# javascript using selenium. The window.scroll method is used to scroll the page.
# Document.body.scrollHeight is used to scroll to the bottom of the page.
print("Reached at the bottom of the page")
time.sleep(2)

print("Take the screen-shot of the page after scroll to bottom of the page")
driver.get_screenshot_as_file("screen-shot.png")    # this is to take the screenshot of the page
print("Screen shot is done")

time.sleep(2)
