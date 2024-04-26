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

print("grab the heading of the page")
print(driver.find_element(By.TAG_NAME, "h1").text)
time.sleep(2)

print("Click on Frame section of the page")
driver.find_element(By.LINK_TEXT, "Frames").click()
time.sleep(2)

print("Page in navigated to another page")
driver.find_element(By.LINK_TEXT, "iFrame").click()
time.sleep(2)

print("Switch to frame")
driver.switch_to.frame("mce_0_ifr")  # this is to swtich into frame to read the element of html because html written
# in frames has to read via frame which means first we need to first move into frame then read the html element

print("Move to frame section of the page")
driver.find_element(By.XPATH, "//body[@id='tinymce']").clear()
print("Text as - > Your content goes here -> is cleared now")

print("After clear write my own sentence into the box")
driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys("My name is Sujeet Sharma")
print("My text added in the frame box")
time.sleep(5)

print("Switch out from the frame to grab  the text-> 'An iFrame containing the TinyMCE WYSIWYG Editor'")
driver.switch_to.default_content()  # this is to move out of the switch other wise
# if any content which is not in frame then ot will throw an error
time.sleep(2)

print("Now grab the text which is not in frame section i.e. -> 'An iFrame containing the TinyMCE WYSIWYG Editor'")
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
