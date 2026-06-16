import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class Orange_hrm(BasePage):
    user_locator=(By.XPATH,'//input[@name="username"]')
    password_locator=(By.XPATH,'//input[@name="password"]')
    submit_locator=(By.XPATH,'//button[@type="submit"]')
    myinfo_locator=(By.XPATH,'//a[@href="/web/index.php/pim/viewMyDetails"]')
    nation_locator=(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div')
    marriage_locator=(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div")
    save_button=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')
    checkbox_button=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span')
    delete_locator=(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin"]')
    delete_confirm_locator=(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')
    contact_locator=(By.XPATH,'//a[contains(text(),"Contact Details")]')
    country_locator=(By.XPATH,'//div[@class="oxd-select-wrapper"]')
    contact_save_locator=(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    work_email_locator=(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]')


    def __init__(self,driver):
        """
        Initialize the base page with the driver.
        Use 'self' inside class methods, NOT 'context'.
        """
        super().__init__(driver)
        # Fetch environment variables safely with fallbacks
        self.url ="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def initial_load(self):
        self.open(self.url)

    def login(self):
        self.type(self.user_locator,'Admin')
        self.type(self.password_locator,'admin123')
        self.click(self.submit_locator)
    def info(self):
        self.click(self.myinfo_locator)
        time.sleep(5)

    # def personal_details(self):
    #     element=self.driver.find_element(self.nation_locator)
    #     dropdown=Select(element)
    #     dropdown.select_by_visible_text('Indian')
    #     marriage_element=self.driver.find_element(self.marriage_locator)
    #     marriage_dropdown=Select(marriage_element)
    #     marriage_dropdown.select_by_visible_text('Married')

    # def save_details(self):
    #     self.click(self.save_button)

    def record_deletion(self):
        self.click(self.checkbox_button)
        self.click(self.delete_locator)
        self.click(self.delete_confirm_locator)
        time.sleep(2)

    def contact_details(self):
        self.click(self.contact_locator)
        element=self.driver.find_element(self.country_locator)
        country_drop=Select(element)
        country_drop.select_by_visible_text('India')
        self.click(self.contact_save_locator)
        time.sleep(5)




