# from dotenv import load_workbook, load_dotenv
from selenium import webdriver

from pages.login_page import LoginPage
from pages.bank_page import Register
from pages.orangehrm_page import Orange_hrm
from pages.cart_page import CartPage


# Load your .env file
# load_dotenv()

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    options.add_argument("--disable-features=PasswordLeakDetection")

    options.add_argument("--disable-features=SafeBrowsing")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-manager-reauthentication")

    prefs = {

        "credentials_enable_service": False,  # Kills the password manager service completely

        "profile.password_manager_enabled": False,  # Suppresses the "Save Password?" banner prompt

        "autofill.profile_enabled": False,  # Turns off address autofill prompts

        "autofill.credit_card_enabled": False  # Turns off credit card autofill prompts

    }

    options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(options=options)

    # Initialize your Page Objects

    context.login_page = LoginPage(context.driver)
    context.bank_page= Register(context.driver)
    context.orangehrm_page=Orange_hrm(context.driver)
    context.cart_page = CartPage(context.driver)
def after_scenario(context, scenario):
    # Teardown driver
    if hasattr(context, 'driver'):
        context.driver.quit()
