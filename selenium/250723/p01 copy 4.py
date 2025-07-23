from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

# element = driver.find_element(By.CSS_SELECTOR, "div.card-body > h4.card-text")
# print(element.text)

elements = driver.find_elements(By.CSS_SELECTOR, "div.card-body > h4.card-text")

for element in elements :
    print(element.text)

time.sleep(1)

driver.quit()