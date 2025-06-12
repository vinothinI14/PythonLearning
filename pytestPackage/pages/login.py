from selenium.webdriver.common.by import By

from Utils.BasePageObject import BaseObjects
from pytestPackage.pages import shop


class LoginPage(BaseObjects):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.userInput =  (By.ID, "username")
        self.passwordInput = (By.ID, "password")
        self.terms = (By.ID, "terms")
        self.signBtn = (By.ID, "signInBtn")

    def login(self,userName,passWord):

        # self.driver.find_element(*self.userInput).send_keys(userName)
        # self.driver.find_element(*self.passwordInput).send_keys(passWord)
        # driver.find_element(By.XPATH, "(//span[@class='checkmark'])[2]").click()
        # self.driver.find_element(*self.terms).click()
        # self.driver.find_element(*self.signBtn).click()
        BaseObjects.setInput(self,self.userInput,userName)
        BaseObjects.setInput(self,self.passwordInput,passWord)
        BaseObjects.click(self,self.terms)
        BaseObjects.click(self,self.signBtn)
