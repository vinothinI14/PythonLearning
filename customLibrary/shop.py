from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class shop:

    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    @keyword
    def hello_world(self):
        print("Welcome to custom library")

    @keyword
    def add_item_and_checkout(self, productList):
        i = 1
        self.selLib.scroll_element_into_view("//h4[@class='card-title']")
        productTitles = self.selLib.get_webelements("//h4[@class='card-title']")
        for productTitle in productTitles:
            title = productTitle.text
            if title in productList:
                self.selLib.click_button("(//button[@class='btn btn-info'])[" + str(i) + "]")
                print("product added :" + title)
        i = i + 1
        self.selLib.click_element("//div[@id='navbarResponsive']//a")


