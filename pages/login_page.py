import os
from pathlib import Path
# from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Load the environment variables globally or inside the init
# load_dotenv(dotenv_path=Path('.').resolve() / '.env')


class LoginPage(BasePage):
    # Locators (Keep as class attributes)
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_text = (By.XPATH, "//h3")

    def __init__(self, driver):
        """
        Initialize the base page with the driver.
        Use 'self' inside class methods, NOT 'context'.
        """
        super().__init__(driver)
        # Fetch environment variables safely with fallbacks
        self.url =  "https://www.saucedemo.com/"
        self.username = "standard_user"
        self.password =  "secret_sauce"
        self.wrongpassword ="wrong_sauce"

    def load(self):
        """Navigates to the page URL."""
        self.open(self.url)

    def login(self, login_type):
        """Performs login based on credential validity type."""
        self.type(self.username_input, self.username)

        if login_type == "valid":
            self.type(self.password_input, self.password)
        else:
            self.type(self.password_input, self.wrongpassword)

        self.click(self.login_button)

    def get_error_text(self):
        """Returns the error message text."""
        return self.get_text(self.error_text)  # Using standard snake_case naming

