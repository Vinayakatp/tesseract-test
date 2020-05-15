from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:

    def __init__(self,driver):
        self.driver = driver


    def get_login(self):
        try:
            return self.driver.find_element_by_link_text("Login")
        except:
            return None

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_id("user_email")
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_id("user_password")
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='alert alert-danger']")
        except:
            return None

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.visibility_of(self.get_username_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_password_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_login_button()))