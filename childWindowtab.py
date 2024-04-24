import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("https://the-internet.herokuapp.com/")
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

print("Click on the option visible on the page !!!")
print("The Heading of the page is ->", driver.find_element(By.TAG_NAME, "h1").text)
time.sleep(2)

driver.find_element(By.LINK_TEXT, "A/B Testing").click()
print("'A/B Testing' option is clicked'")
time.sleep(2)

print("Once 'A/B Testing' option is clicked on parent tab' is opened then grab the text")
print("The paragraph is written on 'A/B Testing' option is clicked' is = ", driver.find_element(By.TAG_NAME, "p").text)
time.sleep(2)

print("Click on 'Elemental Selenium'")
driver.find_element(By.CSS_SELECTOR, "a[target$='_blank']").click()
print("Clicked on 'Elemental Selenium' done")
time.sleep(2)

windowsOpened = driver.window_handles
print("Switch the next tab after click on 'Elemental Selenium' done")
time.sleep(2)

driver.switch_to.window(windowsOpened[1])
print("Next tab opened")
print("The text on new tab = ", driver.find_element(By.CSS_SELECTOR, "div header p").text)
time.sleep(2)

print("Close the child tab and switch back to parent tab")
driver.close()
time.sleep(2)

driver.switch_to.window(windowsOpened[0])

if "A/B Test Control" == driver.find_element(By.TAG_NAME, "h3").text:
    print("Switched over parent tab done")
else:
    print("Stay on child tab")
    driver.switch_to.window(windowsOpened[0])
time.sleep(2)
