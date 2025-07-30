import requests
from bs4 import BeautifulSoup

query = "데이터 분석가"
url = f"https://www.jobkorea.co.kr/Search/?stext={query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("div.styles_mb_space8__dk46ts1p a.sn28bt0")

for i, title_tag in enumerate(titles[:20], 1) :
    print(f"{i}. {title_tag.text.strip()}")