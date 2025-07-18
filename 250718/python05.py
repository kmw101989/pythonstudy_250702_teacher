import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/trial/board/news.html")
soup = BeautifulSoup(res.content, "html.parser")

# datas = soup.select("div.list_content>div.list_item")
datas = soup.select("div.list_item")
index = 0

for data in datas :
    title = data.select_one("span.subject_fixed")
    # print(index + 1, title.get_text().strip())
    if title != None :
        index += 1
        print(index, title.get_text().strip())