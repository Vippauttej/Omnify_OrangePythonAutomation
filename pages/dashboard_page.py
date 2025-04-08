from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_module = (By.XPATH, "//span[text()='PIM']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_module)
        ).click()

    def is_dashboard_displayed(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.pim_module)
            ).is_displayed()
        except:
            return False

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()
