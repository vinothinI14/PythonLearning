from selenium.webdriver.common.by import By

from Utils.BasePageObject import BaseObjects


class ShopPage(BaseObjects):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop = (By.CSS_SELECTOR, " a[href*='shop']")
        self.productcart = (By.XPATH,"//div[@class='card h-100']")
        self.checkoutbtn=(By.XPATH, "//*[contains(text(),'Checkout')]")


    def shop_page(self,expectedProduct):
        self.driver.find_element(*self.shop).click()
        productus = self.driver.find_elements(*self.productcart)

        for product in productus:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == expectedProduct:
                product.find_element(By.XPATH, "div/button").click()


    def goTo_cart(self):
        self.driver.find_element(*self.checkoutbtn).click()
