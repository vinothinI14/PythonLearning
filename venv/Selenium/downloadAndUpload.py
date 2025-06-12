import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def updateExcelData(filePath,fruitName,columnName,newValue):
    wrBook = load_workbook(filepath)
    sheet = wrBook.active
    rowsCount = sheet.max_row
    colsCount = sheet.max_column
    Dict ={}
    for c in range(1, colsCount + 1):
        print(sheet.cell(row=1, column=c).value)
        if sheet.cell(row=1, column=c).value == columnName:
            Dict["col"]=c

    for r in range(1, rowsCount + 1):
            for j in range(1, colsCount + 1):
                if sheet.cell(row=r, column=j).value == fruitName:
                    Dict["row"]=r

    sheet.cell(row=Dict["row"], column=Dict["col"]).value = newValue
    wrBook.save(filepath)

filepath = "C:\\Users\\ADMIN\\Downloads\\download.xlsx"
fruitName= "Papaya"
columnName = "price"
value= "9001"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.ID,"downloadButton").click()
time.sleep(3)
updateExcelData(filepath,fruitName,columnName,value)
driver.find_element(By.ID,"fileinput").send_keys(filepath)
time.sleep(2)

priceColID = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
priceValue=driver.find_element(By.XPATH, "//*[text()='"+fruitName+"']/parent::div/parent::div/div[@id='cell-"+priceColID+"-undefined']")
print(priceValue.text)
actualValue = priceValue.text
assert  actualValue == value


