import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import DrCatalyst_EHR
from utitlities.Logger import LogGenerator


class Test_login_drcatalyst:
    log = LogGenerator.loggen()

    def test_login_page(self, setup):
        self.driver = setup
        self.dc = DrCatalyst_EHR(self.driver)
        self.log.info("Launching the webpage URL")
        self.log.info("Checking the webpage")
        self.dc.Check_Login_page_Message()
        self.log.info("Entering Clinic Number")
        self.dc.Enter_Clinic_number(1234)
        self.log.info("Entering Username")
        self.dc.Enter_Username("pallavi@123")
        self.log.info("Entering Password")
        self.dc.Enter_Password("P@123456")
        self.log.info("Clicking on Login Button")
        self.dc.Click_Login_Button()
        self.log.info("Checking the login Success message")

        if self.dc.Error_Msg() == True:
            allure.attach(self.driver.get_screenshot_as_png(),name="test-login_invalid_credentials_pass",attachment_type=AttachmentType.PNG)
            print("Login Unsuccessful with Invalid Credentials")
            return True
        else:
            print("Login Successful")
            return False
