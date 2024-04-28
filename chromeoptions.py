from selenium import webdriver
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("-ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://stackoverflow.com/questions/12698843/how-do-i-pass-options-to-the-selenium-chrome-driver-using"
           "-python")


print(driver.title)
