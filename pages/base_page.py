from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def wait_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open(self,url):
        self.driver.get(url)

    def click(self,locator):
        self.wait_clickable(locator).click()

    def type(self,locator,text):
        element=self.wait_visible(locator)
        # if clear_first:
        #     element.clear()
        element.send_keys(text)

    def getText(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text