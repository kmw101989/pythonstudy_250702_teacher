from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

element = driver.find_element(By.NAME, "EMAIL")
element.clear()

element.send_keys("error@error.com")

time.sleep(3)

element.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()