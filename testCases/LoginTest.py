import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("C://Users/HP/Google Drive/Learning/PomBasedUnittestProject")
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    usernam=" "
    password=" "
    driver=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.usernam)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users/HP/Google Drive/Learning/PomBasedUnittestProject/Reports"))