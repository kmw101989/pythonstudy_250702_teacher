import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/trial/board/news.html")
soup = BeautifulSoup(res.content, "html.parser")

datas = soup.select("div.list_item")
index = 0

for data in datas :
    title = data.select_one("span.subject_fixed")
    replies = data.select_one("span.rSymph05")
    link = data.select_one("a.list_subject")
    if title != None :
        index += 1
        print(index, title.get_text().strip(), replies.get_text(), "https://davelee-fun.github.io/trial/board/"+link["href"])