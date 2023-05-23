import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
"""
Comment captez un screenshot
"""
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/overview/components/")
driver.save_screenshot("C:\\Users\\Soumaya\\PycharmProjects\\seleniumProject2\\jour3\\selenium.png")
driver.save_screenshot(os.getcwd()+"\\selenium2.png")
time.sleep(5)
