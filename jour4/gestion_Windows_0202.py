import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By

#instanciation de l'objet chrome et on le stock dans une variable drive
driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
footer = driver.find_element(By.CLASS_NAME,"orangehrm-login-footer-sm")
liste_liens=footer.find_elements(By.TAG_NAME,"a")
for lien in liste_liens:
    lien.click()

# ids_footer=driver.window_handles
# id_youtube=ids_footer[4]
# driver.switch_to.window(id_youtube)
# youtube_titre=driver.title
# youtube_url=driver.current_url
# print(youtube_titre,"\n",youtube_url)

ids=driver.window_handles
for winId in ids:
    driver.switch_to.window(winId)
    if driver.title=="OrangeHRM Inc - YouTube":
        print(driver.title,"***********",driver.current_url)


time.sleep(3)
driver.quit()