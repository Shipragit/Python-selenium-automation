from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "user_name")
        self.password_input = (By.ID, "user_password")
        self.lgnBtn = (By.ID, "sysverb_login")
        self.wait = WebDriverWait(self.driver, 60)

    def login(self,username,password):
        self.driver.get("https://brightspeedtsmuat.service-now.com/login.do")
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.lgnBtn).click()
        #self.wait.until(EC.title_contains("Dashboards Overview | ServiceNow"))