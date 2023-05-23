#https://the-internet.herokuapp.com/javascript_alerts
#//button[@onclick='jsAlert()']
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
time.sleep(3)
alerte = driver.switch_to.alert
print(alerte.text)
time.sleep(5)
alerte.accept()
time.sleep(5)
driver.quit()