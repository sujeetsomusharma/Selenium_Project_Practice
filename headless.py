# ---------- About Headless -------------
# In software development, "headless" typically refers to a system or application that operates without a graphical
# user interface (GUI). In other words, it doesn't have a traditional visual interface that users interact with
# directly. Instead, it is controlled and accessed programmatically or through other interfaces like APIs (
# Application Programming Interfaces) or command-line interfaces (CLI). Headless systems are often used in server
# environments, where there's no need for human interaction with the software directly. They are common in web
# development, where headless browsers are used for tasks like web scraping, automated testing, or rendering web
# pages for different purposes without the need for a visible browser window. Headless systems can offer benefits
# such as better performance, reduced resource consumption, and increased flexibility in how they can be integrated
# into larger systems or workflows.

# --------- About --ignore-certificate-errors --------------- The --ignore-certificate-errors flag is a command-line
# option used with web browsers, particularly Google Chrome and Chromium-based browsers like Microsoft Edge, Brave,
# and others. When this flag is set, the browser disregards SSL certificate errors when accessing HTTPS websites. SSL
# (Secure Sockets Layer) certificates are used to establish a secure encrypted connection between a web server and a
# web browser. They ensure that the data exchanged between the server and the browser remains private and integral.
# However, there are situations where SSL certificate errors occur, such as: The certificate has expired. The
# certificate is self-signed or issued by an untrusted Certificate Authority (CA). The hostname on the certificate
# does not match the website's domain name. In development or testing environments, developers may encounter SSL
# certificate errors, especially when working with self-signed certificates or testing on local servers. In such
# cases, using the --ignore-certificate-errors flag can be helpful as it allows the browser to continue loading the
# page despite encountering certificate errors. It's important to note that using this flag bypasses SSL certificate
# validation, which could expose users to security risks, particularly in production environments. Therefore,
# it should only be used for testing or development purposes and not in production system


import time
from datetime import datetime
import document
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.select import Select

current_time = datetime.now()
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")  # this is for to stop to envoke the browser
# and only the execution will run in background

chrome_option.add_argument("--ignore-certificate-errors")  # this is a flag to ignore the ssl certificate error option
# like we need to click on advance option and then click on proceed now with the url.

driver = webdriver.Chrome(options=chrome_option)
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
driver.get_screenshot_as_file("screen-shot.png")  # this is to take the screenshot of the page
print("Screen shot is done at = ",current_time )

time.sleep(2)
