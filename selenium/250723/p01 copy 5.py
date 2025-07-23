from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

# element = driver.find_element(By.CSS_SELECTOR, "a.text-dark")
# print("text : ", element.text)
# print("driver.title : ", element.get_attribute("href"))
# print("get_attribute('class') : ", element.get_attribute("class"))
# print("get_attribute('text') : ", element.get_attribute("text"))

elements = driver.find_elements(By.CSS_SELECTOR, "a.text-dark")
for element in elements :
    print("text : ", element.text)
    print("driver.title : ", element.get_attribute("href"))
    print("get_attribute('class') : ", element.get_attribute("class"))
    print("get_attribute('text') : ", element.get_attribute("text"))

time.sleep(1)

driver.quit()