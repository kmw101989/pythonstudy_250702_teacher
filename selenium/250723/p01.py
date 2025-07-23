from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# pip install webdriver-manager
# pip show webdriver-manager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

# print(driver.title)
# print(driver.current_url)

assert "Teddy" in driver.title

time.sleep(1)

driver.quit()