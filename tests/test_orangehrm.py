import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        cls.login_page = LoginPage(cls.driver)
        cls.dashboard_page = DashboardPage(cls.driver)
        cls.pim_page = PIMPage(cls.driver)

    def test_01_login(self):
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login_button()
        self.assertTrue(self.dashboard_page.is_dashboard_displayed())

    def test_02_add_employees(self):
        for fname, lname in [("Sai", "ss"), ("shailu", "sm"), ("Bhanu", "kk"), ("shravs", "ll")]:
            self.dashboard_page.navigate_to_pim()
            self.pim_page.add_employee(fname, lname)

    def test_03_verify_employees(self):
        for name in ["Sai", "shailu", "Bhanu", "shravs"]:
            self.dashboard_page.navigate_to_pim()
            self.assertTrue(self.pim_page.verify_employee(name))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
