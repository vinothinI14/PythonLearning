import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#HEadless mode execution
chromeOption = webdriver.ChromeOptions()
chromeOption.add_argument("headless")

service_obj = Service("C:/Users/ADMIN/Desktop/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chromeOption)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

