
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#https://www.orangehrm.com/
#instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#--------------------------------
login_URL = driver.current_url
URL_Attendu = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" #manuellement
assert login_URL==URL_Attendu,"L'URL de la page ne correspond pas a l'URL attendu."


#----------------------------------
login_title = driver.title #Script
Title_Attendu = "OrangeHRM"   #manuellement
assert login_title==Title_Attendu , "Le titre de la page ne correspond pas au titre attendu."
#------------------------------------
print (login_title," ",login_URL)
ID_parent = driver.current_window_handle
print(ID_parent)
time.sleep(4)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
IDs = driver.window_handles
ID_login =IDs[0]
ID_home =IDs[1]
print(ID_login,"   ****   ",ID_home)

driver.switch_to.window(ID_home)
home_URL = driver.current_url
home_URL_Attendu = "https://www.orangehrm.com/" #manuellement
assert home_URL==home_URL_Attendu,"L'URL de la page ne correspond pas a l'URL attendu."
driver.switch_to.window(ID_login)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(4)
driver.quit()
