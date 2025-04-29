from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("javatpoint")
search_box.send_keys(Keys.ENTER)

time.sleep(30)
driver.close()
print("Sample test Successful")
