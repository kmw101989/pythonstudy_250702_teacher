from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service("C:\\Users\\user\\Downloads\\chromedriver\\chromedriver.exe")
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service = service, options = options)

driver.get("https://davelee-fun.github.io/")

# element = driver.find_element(By.ID, "navbarMediumish")
# print(element.text)

elements = driver.find_elements(By.ID, "navbarMediumish")

for element in elements :
    print(element.text)

time.sleep(1)

driver.quit()