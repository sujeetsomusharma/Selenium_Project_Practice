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
time.sleep(1)

driver.maximize_window()
print("---Window maximize---")
time.sleep(1)

print("---The Title of the page is---")
print("The tile is = ", driver.title)
time.sleep(1)

print("---The url of the page is--- ")
print("The url of the page is = ", driver.current_url)
time.sleep(1)

# checkbox can be done is multiple ways like below
# this is method one

'''print("Select the checkbox")
driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click()
print("Option 1 is selected")
time.sleep(2)'''

print("Select the checkbox ")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        # to check is option is selected or not we have a method -> is.selected()
        print(checkbox.is_selected())
        assert checkbox.is_selected()
        break
print("Checkbox option 3 is selected")
time.sleep(2)

# multiple radiobutton can be done is multiple ways like below
# this is method 1
print("Select the radio button")

''' radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radiobutton in radio_buttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        # to check is option is selected or not we have a method -> is.selected()
        print(radiobutton.is_selected())
        assert radiobutton.is_selected()
        break
print("radiobutton option 2 is selected") '''

# this is method 2

radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
radio_buttons[1].click()
print("Is Radio button option 2 is selected = ", radio_buttons[1].is_selected())
time.sleep(1)

# is_display method

display_text_hide_show = driver.find_element(By.ID, "displayed-text")
print("Is text in show and hide is visible in box = ", display_text_hide_show.is_displayed())  # this will return
# true as hide button is not clicked first

print("Hide option is clicked",
      driver.find_element(By.ID, "hide-textbox").click())  # now option is hide button is clicked

print("Is text in show and hide is visible in box = ", display_text_hide_show.is_displayed())  # this will return
# false as hide button is clicked

time.sleep(5)

print("Clicked on show button")
driver.find_element(By.ID, "show-textbox").click()  # clicked on show button
print("Show option is clicked", display_text_hide_show.is_displayed())

time.sleep(5)
