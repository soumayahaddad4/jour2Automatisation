
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
time.sleep(4)
#driver.find_element(By.CLASS_NAME,"orangehrm-login-footer-sm").find_element(By.TAG_NAME,"a").click()
footer = driver.find_element(By.CLASS_NAME,"orangehrm-login-footer-sm")

liste_Liens = footer.find_elements(By.TAG_NAME,"a")
print(liste_Liens)
print(len(liste_Liens))
IDs = driver.window_handles
print(IDs)
print(len(IDs))
time.sleep(2)
for i in range(0,4):
    liste_Liens[i].click()
    time.sleep(4)
    new_ID = driver.current_window_handle
    IDs.append(new_ID)  # Ajouter le nouvel identifiant à la liste IDs
    print(IDs[i])
    #print(IDs[i+1])
    time.sleep(4)
    #driver.switch_to.window(IDs[i+1])
    #time.sleep(4)
    current_page_title = driver.find_element(By.TAG_NAME,"head")
    time.sleep(4)
    print(current_page_title)


time.sleep(10)

driver.quit()
