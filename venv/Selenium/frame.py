from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT, "JOIN NOW").click()
driver.switch_to.default_content()
