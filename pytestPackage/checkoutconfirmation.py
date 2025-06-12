from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.BasePageObject import BaseObjects


class Checkoutconfirmation(BaseObjects):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.gocart = (By.XPATH, "//*[contains(text(),'Checkout')]")
        self.countryInput =(By.ID, "country")
        self.country = (By.LINK_TEXT, "India")
        self.terms = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchasebtn =(By.XPATH, "//input[@value='Purchase']")
        self.sucessmsg = (By.XPATH, "//*[contains(text(),'Success!')]")


    def checkoutprduct(self):
        self.driver.find_element(*self.gocart).click()


    def enterdeliveryaddress(self,countryName):
        self.driver.find_element(*self.countryInput).send_keys(countryName)
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((self.country)))
        self.driver.find_element(*self.country).click()
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.purchasebtn).click()


    def validateorder(self):
        successmessage = self.driver.find_element(*self.sucessmsg).text
        assert "Success" in successmessage