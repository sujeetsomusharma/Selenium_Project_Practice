# browser base alert pop


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

name = "Sujeet"

print("Enter the text in 'Switch to' Alert Example ")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
print("Name is entered")
time.sleep(2)
print("Click on alert button")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
time.sleep(2)
print("Click on alert button is done")
time.sleep(2)

# once the click on alert button is done then a pop up will
# appear but the pop is not understood by selenium webdriver
# because selenium web driver only understood the html code not the JS
# for this we need to switch from browser mode to alert mode

alert = driver.switch_to.alert  # this is a method to switch form browser to alert mode to read the content of the
# alert popup
alert_text = alert.text  # this text method is to grab the text on the alert pop up
print("The text on the alert pop up is  = ", alert_text)

print(name, "is the name on pop alert text")

name_available = alert_text[6:12]
if name_available == name:
    print("Click on Okay is Done", alert.accept())  # this is to click on Okay button on pop up alert
else:
    print("Click on cancel as name is not available", alert.dismiss())  # this is to click on cancel button on pop up
    # alert

print("End of Code")
