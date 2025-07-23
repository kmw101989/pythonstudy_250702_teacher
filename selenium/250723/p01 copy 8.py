from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, 2155)")

time.sleep(1)

driver.quit()