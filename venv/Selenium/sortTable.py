from selenium import webdriver
from selenium.webdriver.common.by import By

browsersortedList=[]
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.XPATH, "(//th[@role='columnheader']//span)[2]").click()
table = driver.find_element(By.XPATH, "//table[ contains(@class,'table-bordered')]")
tableBody =table.find_element(By.TAG_NAME, "tbody")
rows = tableBody.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    browsersortedList.append(cols[0].text)
originalSortedList = browsersortedList.copy() #Copy list to another list
print(originalSortedList)
print(browsersortedList.copy())
browsersortedList.sort()
assert originalSortedList == browsersortedList
