from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
action.context_click(driver.find_element(By.XPATH, "//*[text()='Mouse Hover Example']")).perform()

