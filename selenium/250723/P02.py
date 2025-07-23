from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

service = Service(ChromeDriverManager().install())

options = Options()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("--disable-gpu")
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(service = service, options = options)
driver.get("https://davelee-fun.github.io/")

element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

time.sleep(3)

driver.quit()