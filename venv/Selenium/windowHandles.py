from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, "Open Tab").click()
windows = driver.window_handles
len(windows)
driver.switch_to.window(windows[1])
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Courses")))
driver.find_element(By.LINK_TEXT, "Courses").click()
driver.close()
driver.switch_to.window(windows[0])
print(driver.find_element(By.CLASS_NAME, "switch-tab").text)
