
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

service = Service(ChromeDriverManager().install())

prefs = {
    "credentials_enable_service": False, # 크롭 웹 브라워 자체 로그인 팝업 비활성화
    "profile.password_manager_enabled": False # 비밀번호 저장 팝업 끄기
}

options = Options()
# options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-gpu")
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(service = service, options = options)
driver.get("https://divjason.github.io/sellenium-test/index.html?")

element = driver.find_element(By.ID, "username")
element.clear()
element.send_keys("error@error.com")

element = driver.find_element(By.ID, "password")
element.clear()
element.send_keys("1234")

time.sleep(3)

# element.send_keys(Keys.RETURN)
element = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
element.click()
time.sleep(3)

element1 = driver.find_element(By.CSS_SELECTOR, "div.message")
print(element1.text)

element = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
element.click()

driver.get("https://divjason.github.io/sellenium-test/index.html?")

element2 = driver.find_element(By.CSS_SELECTOR, "div.message")
print(element2.text)

driver.quit()