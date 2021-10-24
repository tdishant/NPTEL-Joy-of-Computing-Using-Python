from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/mac/Downloads/chromedriver")

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

target = '"Manav Shah (Mob)"'#the contact to whom you want to send message

msg = "Message sent using Python!!"#message to be sent

x_args = '//span[contains(@title, '+ target + ')]'

target = wait.until(EC.presence_of_element_located((By.XPATH, x_args)))
target.click()

input_box = driver.find_element_by_class_name("p3_M1")

for i in range(5):
    input_box.send_keys(msg + Keys.ENTER)