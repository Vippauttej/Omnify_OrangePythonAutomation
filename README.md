# Omnify_OrangePythonAutomation

# Selenium POM - OrangeHRM Login Automation

This project demonstrates how to automate login functionality of [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/) using **Selenium WebDriver** with **Python** and **Page Object Model (POM)** design pattern.

---

## 📁 Project Structure
orangehrm_pom/ ├── pages/ │ 
                   ├── dashboard_page.py # Dashboard page class with common methods │ 
                   └── login_page.py # Page class for login page actions
                    ├── pim_page.py # Script to manually test login functionality
              ├──tests/ |
                  |__test_orangeHRM   #How to Do Test  and Data to be tested
      └── README.md # Project documentation

---
##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vippauttej/Omnify_OrangePythonAutomation.git
cd orangehrm-pom


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



install Dependencies :

### pip install selenium


Download the ChromeDriver that matches your installed Chrome version:

🔗 https://sites.google.com/a/chromium.org/chromedriver/downloads

Place it in the project root folder or add it to your system PATH.

### Run the Test

python test_Orangehrm.py > run

