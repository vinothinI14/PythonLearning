class BaseObjects:

    def __init__(self,driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title


    def click(self,element):
        self.driver.find_element(*element).click()

    def setInput(self,element,inputValue):
        self.driver.find_element(*element).send_keys(inputValue)
