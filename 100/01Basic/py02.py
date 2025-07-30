import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/tech"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("ul.list_newsheadline2 li a.item_newsheadline2")

for i, article in enumerate(articles, 1) :
    title = article.text.strip()
    link = article["href"]
    print(f"{i}. {title} - {link}")