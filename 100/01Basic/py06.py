from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse
import pandas as pd

service = Service(ChromeDriverManager().install())

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--start-maximized")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")
options.add_argument("--lang=ko_KR")

driver = webdriver.Chrome(service=service, options=options)

query = "데이터 분석가"
encoded_query = urllib.parse.quote(query)

max_pages = 6

results = []

for page in range(1, max_pages + 1) :
    url = f"https://www.jobkorea.co.kr/Search?stext={encoded_query}&Page_No={page}&local=I000&tabType=recruit&careerType=1"
    driver.get(url)
    time.sleep(2)

    job_posts = driver.find_elements(By.CSS_SELECTOR, "div.styles_mb_space8__dk46ts1p")
    for post in job_posts :
        try :
            title_elem = post.find_element(By.CSS_SELECTOR, "a.sn28bt0")
            title = title_elem.text.strip()
            link = title_elem.get_attribute("href")
            results.append({
                "제목" : title,
                "지원링크" : link
            })
        except :
            continue
            
driver.quit()

df = pd.DataFrame(results)
df.to_excel("잡코리아_데이터분석가_서울_신입_3페이지.xlsx", index=False)
print("엑셀 저장 완료!")