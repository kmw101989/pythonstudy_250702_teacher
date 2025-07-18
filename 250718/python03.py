import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawling_stock_example.html")
soup = BeautifulSoup(res.content, "html.parser")

datas = soup.select("ul.table-stock.sty1>li.row_sty")

for data in datas :
    company = data.select_one("div.st_name").get_text().strip().replace(" ", "").replace("\n", "")
    price = data.select_one("div.st_price").get_text().strip().replace(" ", "")
    rate = data.select_one("div.st_rate").get_text().strip().replace(" ", "").replace("\n", "")
    print(f"{company} : {price}원 / {rate}")