from selenium import webdriver
import unittest
import sys
import path

# directory reach
directory = path.path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)

# sys.path.insert(0,r'D:\AUTO_TC\ST_IM_PERSONA_PROD\Object_Repository')
# sys.path.insert(0,r'D:\AUTO_TC\ST_IM_PERSONA_PROD\Keywords')
# sys.path.insert(0,r'D:\AUTO_TC\Python_Reusable_Utilities')
from Object_Repository import utilities_imdb
from Sign_In_Page import SignIN
from Common_Keywords import CmnKeywords
from Home_Page import Home

class TestSuiteIMDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result =''

    def setUp(self):
        print("This is set up method")
        self.driver = webdriver.Chrome(executable_path=utilities_imdb.chrome_driver_path)
        self.driver.get(utilities_imdb.url)
        print("Launched URL")
        self.signobj = SignIN(self.driver,10)
        self.cmnfnobj = CmnKeywords()
        self.homeobj = Home(self.driver,40)

    def test_01_positive_login(self):
        print("1st test case")
        self.signobj.fn_verify_title()
        input_data = self.cmnfnobj.read_data('TC_01')
        user_id=input_data[0]
        pasword = input_data[1]
        role = input_data[2]
        status = self.signobj.fn_login(user_id,pasword,role)
        if status == 'Passed':
            print("TC finished")
            self.result = 'Passed'
        else:
            print("TC Failed")
            self.result = 'Failed'


    def test_02_add_wtchlst_movie(self):
        print("2nd test case")
        self.signobj.fn_verify_title()
        input_data = self.cmnfnobj.read_data('TC_02')
        print(input_data)
        user_id = input_data[0]
        pasword = input_data[1]
        role = input_data[2]
        status = self.signobj.fn_login(user_id, pasword, role)
        if status == 'Passed':
            st_lgout = self.homeobj.fn_logout()
            if st_lgout == 'Passed':
                print("TC finished")
                self.result = 'Passed'
            else:
                print("TC Failed")
                self.result = 'Failed'
        else:
            print("TC Failed as login failed")

    def tearDown(self):
        print("This is tear down method")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # print(f"TC Result = {cls.result}")
        pass

if __name__ =="__main__":
    unittest.main()
