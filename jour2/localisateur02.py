import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"oxd-topbar-header-breadcrumb-module").is_displayed()
Dashboard=driver.find_element(By.CLASS_NAME,"oxd-topbar-header-breadcrumb-module").text
print(Dashboard)
assert "Dashboard" in Dashboard
assert Dashboard =="""Dashboard"""
time.sleep(5)
driver.quit()