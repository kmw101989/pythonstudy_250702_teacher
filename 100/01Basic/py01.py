import requests
from bs4 import BeautifulSoup

query = "디지털 마케팅"
url = f"https://search.naver.com/search.naver?where=news&query={query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("a.ox1N67gcMkHhMh7hbfHi.VZxw34rcBHTWHgERxv0b")

for i, title in enumerate(titles[:10], 1) :
    print(f"{i}. {title.text.strip()}")