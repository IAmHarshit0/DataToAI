from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.find_element(By.ID, "APjFqb")
input_element.send_keys("Harshit" + Keys.ENTER)


time.sleep(10)

driver.quit()