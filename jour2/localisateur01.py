import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.maximize_window()
time.sleep(1)
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.find_element(By.ID,"Email").send_keys("soumaya1.haddad@gmail.com")
driver.find_element(By.ID,"Password").send_keys("123456")
driver.find_element(By.CLASS_NAME,"login-button").click()
driver.find_element(By.CLASS_NAME,"validation-summary-errors").is_displayed()
textError=driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
print(textError)
#assert "Login was unsuccessful." in textError
assert textError =="""Login was unsuccessful. Please correct the errors and try again.
No customer account found"""
time.sleep(5)
driver.quit()