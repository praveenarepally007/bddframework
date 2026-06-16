import time
from operator import countOf

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Register(BasePage):
    # url="https://parabank.parasoft.com/parabank/index.htm"
    register_button=(By.XPATH,'//*[@id="loginPanel"]/p[2]/a')
    f_input=(By.ID,'customer.firstName')
    l_input=(By.ID,'customer.lastName')
    address_input=(By.ID,'customer.address.street')
    city_input=(By.ID,'customer.address.city')
    state_input=(By.ID,'customer.address.state')
    zip_input=(By.ID,'customer.address.zipCode')
    phone_number_input=(By.ID,'customer.phoneNumber')
    ssn_number_input=(By.ID,'customer.ssn')
    username_input=(By.ID,'customer.username')
    password_input=(By.ID,'customer.password')
    confirm_password_input=(By.ID,'repeatedPassword')
    final_register=(By.CLASS_NAME,'button')
    username_login_input=(By.XPATH,'//input[@name="username"]')
    passwd_login_input=(By.XPATH,'//input[@name="password"]')
    login_button_input=(By.XPATH,'//input[@value="Log In"]')
    account_overview_button_locator=(By.XPATH,'//a[@href="overview.htm"]')
    total_amount_locator=(By.XPATH,'//table[@id="accountTable"]//tbody//tr[2]')
    transfer_funds_button=(By.XPATH,'//a[@href="transfer.htm"]')
    amount_input=(By.XPATH,'//input[@id="amount"]')
    final_transfer_button=(By.XPATH,'//input[@type="submit"]')
    def __init__(self,driver):
        """
        Initialize the base page with the driver.
        Use 'self' inside class methods, NOT 'context'.
        """
        super().__init__(driver)
        # Fetch environment variables safely with fallbacks
        self.url ="https://parabank.parasoft.com/parabank/index.htm"
    def load(self):
        self.open(self.url)
    def open_registration(self):
        self.click(self.register_button)
    def initial_registration(self):
        self.type(self.f_input,'king')
        self.type(self.l_input,'a')
        self.type(self.address_input,'street')
        self.type(self.city_input,'city')
        self.type(self.state_input,'state')
        self.type(self.zip_input,'12345')
        self.type(self.phone_number_input,'123')
        self.type(self.ssn_number_input,'1234')
        self.type(self.username_input,'king')
        self.type(self.password_input,'king')
        self.type(self.confirm_password_input,'king')
        self.click(self.final_register)

    def user_login(self):
        self.type(self.username_login_input,'king')
        self.type(self.passwd_login_input,'king')
        self.click(self.login_button_input)
        time.sleep(5)

    def account_overview(self):
        self.click(self.account_overview_button_locator)
        assert self.getText(self.total_amount_locator)=="Total $515.50"


    def transfer_funds(self):
        self.click(self.transfer_funds_button)
        self.type(self.amount_input,'100')
        self.type(self.final_transfer_button)