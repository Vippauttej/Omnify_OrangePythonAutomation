from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (
            By.XPATH, "//button[@type='button' and contains(@class, 'oxd-button--secondary')]")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
        self.employee_search = (
            By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.employee_rows = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    def add_employee(self, first_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_employee_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)

        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

        # Optional: Wait for "Personal Details" page or some confirmation
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
        )

    def verify_employee(self, expected_name):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.employee_search)
            ).clear()

            self.driver.find_element(*self.employee_search).send_keys(expected_name)
            self.driver.find_element(*self.search_button).click()

            time.sleep(2)  # Optionally use explicit wait for table rows to appear

            rows = self.driver.find_elements(*self.employee_rows)
            for row in rows:
                name_cell = row.find_element(By.XPATH, ".//div[3]")  # column index may vary
                actual_name = name_cell.text.strip()
                print(f"Found: {actual_name}")  # Debug log
                if actual_name.lower() == expected_name.lower():
                    return True
        except Exception as e:
            print(f"Exception in verify_employee: {e}")
        return False
