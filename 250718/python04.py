import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/trial/board/news.html")
soup = BeautifulSoup(res.content, "html.parser")

datas = soup.select("div.list_content>div.list_item")

for data in datas :
    title = data.select_one("span.subject_fixed")
    if title != None :
        print(title.get_text().strip())