from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, expected_conditions
from selenium.webdriver.support.ui import Select
import time

#Download chrome driver manually and pass the path in service

# service_obj = Service("C:/Users/ADMIN/Documents/Driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://chatgpt.com/")

#Automatically download driver and invoke
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(3)
# driver.find_element(By.ID, "name").send_keys("Vinothini")
# driver.find_element(By.ID, "email").send_keys("vinothiniaut09@mai.com")
# driver.find_element(By.ID, "agreeTerms").click()
# driver.find_element(By.ID, "form-submit").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//input[@class='search-keyword']").click()
driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("Cu")
driver.find_element(By.XPATH, "//button[@class='search-button']").click()
time.sleep(2)

pExpectedList =["Cucumber - 1 Kg","Capsicum"]
pActualList = []
productLists = driver.find_elements(By.XPATH, "//div[@class='product']")
assert len(productLists) >0
print(len(productLists))
for product in productLists:
    pActualList.append(product.find_element(By.XPATH, "h4").text)

assert pExpectedList == pActualList
addToCart = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
for cart in addToCart:
    cart.click()
driver.find_element(By.CLASS_NAME, "cart-icon").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(2)

tableBody = driver.find_element(By.XPATH, "//table[@id='productCartTables']//tbody")
rows = tableBody.find_elements(By.TAG_NAME, "tr")
total = 0
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    total = total+ int(cols[4].text)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
codeValidation = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
assert codeValidation == "Code applied ..!"
print("Promo code applied successfully")

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "totAmt")))
totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "discountAmt")))
totalAfDiscount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert totalAmount>totalAfDiscount
print("Discount applied successfully")

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
# time.sleep(2)
selectCountry = driver.find_element(By.XPATH, "//label[text()='Choose Country']/following-sibling::div//select")
country = Select(selectCountry)
country.select_by_index(1)
# time.sleep(2)
agree = driver.find_element(By.CSS_SELECTOR, ".chkAgree")
agree.click()
assert agree.is_selected()
# time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
time.sleep(2)