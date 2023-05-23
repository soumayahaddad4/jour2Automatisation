import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# service_obj = Service("C:\\Users\\Soumaya\\Desktop\\Driver\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.selenium.dev/documentation/overview/components/")
# driver.maximize_window()
# time.sleep(5)
# driver.close()
class ChromeService:
    pass


# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/overview/components/")
#driver.find_element(By.LINK_TEXT,"Watch the Videos").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"the Videos").get_attribute("href")
attributDuLien=driver.find_element(By.LINK_TEXT,"Watch the Videos").get_attribute("href")
print(attributDuLien)
attributDuTarget= driver.find_element(By.LINK_TEXT,"Watch the Videos").get_attribute("target")
print(attributDuTarget)
assert attributDuTarget == "_blank"
driver.find_element(By.LINK_TEXT,"Watch the Videos").is_displayed()
time.sleep(5)
driver.close()