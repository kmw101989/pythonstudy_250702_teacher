from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://davelee-fun.github.io/")

elements = driver.find_elements(By.TAG_NAME, "h4")

for element in elements :
    print(element.text)

time.sleep(1)

driver.quit()