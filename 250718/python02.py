import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawling_stock_example.html")
soup = BeautifulSoup(res.content, "html.parser")

datas = soup.select("ul.table-stock.sty1>li.row_sty")

for data in datas :
    print(data.select_one("div.st_name").get_text().strip().replace(" ", ""))