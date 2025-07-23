from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
height = driver.execute_script("return document.body.scrollHeight")
print("scrollHeight : ", height)

client_height = driver.execute_script("return document.documentElement.clientHeight")
print("clientHeight : ", client_height)

offset_height = driver.execute_script("return document.body.offsetHeight")
print("offsetHeight : ", offset_height)

time.sleep(1)

driver.quit()