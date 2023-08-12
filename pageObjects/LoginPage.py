from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class DrCatalyst_EHR:
    object_clinic_xpath = (By.XPATH, "//mtab-input-text[@id='clinic']//input[@type='TEXT']")
    object_username_xpath = (By.XPATH, "//mtab-input-text[@id='username']//input[@type='TEXT']")
    object_password_xpath = (By.XPATH, "//input[@type='PASSWORD']")
    object_error_msg = (By.XPATH, "//span[@class='mtab-login-error-message']")
    object_welcome_msg = (By.XPATH, "//h2[@class='mtab-login-iemo-welcome']")
    object_login_button = (By.XPATH, "//span[@class='ui-button-text ui-clickable']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Check_Login_page_Message(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.object_welcome_msg))
        welcome_message = self.driver.find_element(*DrCatalyst_EHR.object_welcome_msg).text
        print(welcome_message)

    def Enter_Clinic_number(self, clinic_number):
        self.driver.find_element(*DrCatalyst_EHR.object_clinic_xpath).send_keys(clinic_number)

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.object_welcome_msg))
        self.driver.find_element(*DrCatalyst_EHR.object_username_xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*DrCatalyst_EHR.object_password_xpath).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*DrCatalyst_EHR.object_login_button).click()

    def Error_Msg(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.object_error_msg))
            error_msg = self.driver.find_element(*DrCatalyst_EHR.object_error_msg).text()
            print(error_msg)
            return True
        except:
            return False
