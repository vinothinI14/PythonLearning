import json
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytestPackage import checkoutconfirmation, checkoutconfirmation
from pytestPackage.checkoutconfirmation import Checkoutconfirmation
from pytestPackage.pages.login import LoginPage
from pytestPackage.pages.shop import ShopPage

current_dir = os.path.dirname(__file__)
test_Data_Path = os.path.join(current_dir, '..','Data', 'test_EndToEndPractice.json')
# test_Data_Path = '..\\Data\\test_EndToEndPractice.json'
with open(test_Data_Path) as reader:
    test_data = json.load(reader)
    test_data_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_data_item", test_data_list)
def test_endtoend(launchbrowser,test_data_item):


    driver = launchbrowser
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    loginpage.login(test_data_item["userName"],test_data_item["passWord"])
    shoppage = ShopPage(driver)
    shoppage.shop_page(test_data_item["productName"])
    shoppage.goTo_cart()
    checkoutconfirmation = Checkoutconfirmation(driver)
    checkoutconfirmation.checkoutprduct()
    checkoutconfirmation.enterdeliveryaddress(test_data_item["country"])
    checkoutconfirmation.validateorder()



