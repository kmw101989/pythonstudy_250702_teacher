import requests
from bs4 import BeautifulSoup

url = "https://www.yes24.com/product/category/steadyseller?categoryNumber=001001025007"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("ul#yesBestList > li")



for i, book in enumerate(books[:10], 1) :
    title_tag = book.select_one("div.info_row.info_name a.gd_name")
    author_tag = book.select_one("span.authPub.info_auth")

    if title_tag and author_tag :
        title = title_tag.text.strip()
        author = author_tag.text.strip()
        print(f"{i}. {title} - {author}")