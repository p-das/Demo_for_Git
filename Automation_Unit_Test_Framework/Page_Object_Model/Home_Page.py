from Object_Repository import objectrepository_imdb as OR
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Base_Page import BasePage

class Home(BasePage):

    def fn_logout(self):
        try:
            '''Sign Out'''
            acnt_ele = self.element_locator(OR.account_xpath)
            acnt_ele.click()
            sign_out_ele = self.element_locator(OR.sign_out_xpath)
            sign_out_ele.click()
            sign_in_ele = self.element_locator(OR.sign_in_xpath)
            print("Clicked on Account dropdown")
            if sign_in_ele.is_displayed():
                print("Sign Out Successful")
                status = 'Passed'
            else:
                print("Sign Out Unuccessful")
                status='Failed'
        except Exception as e:
            print(f"Logout unsuccessful. Error:{e}")
            status = 'Failed'
        return status