import requests
from bs4 import BeautifulSoup

url = "https://www.weather.go.kr/w/weather/forecast/short-term.do"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

summary_tag = soup.select_one("div.cmp-view-content > p.summary > span.depth_1")

if summary_tag :
    print("오늘의 전국 날씨 요약 : ")
    print(summary_tag.text.strip())
else :
    print("날씨 요약 정보를 찾을 수 없습니다!")