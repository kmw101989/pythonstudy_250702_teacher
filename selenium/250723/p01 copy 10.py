from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://davelee-fun.github.io/")

screen_width, screen_height = pyautogui.size()
driver.set_window_size(screen_width, screen_height)

element = driver.find_element(By.TAG_NAME, "body")
element.screenshot("samplesite.png")

time.sleep(3)

driver.quit()