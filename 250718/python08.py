import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/trial/board/news.html")
soup = BeautifulSoup(res.content, "html.parser")

datas = soup.select("div.list_item")
index = 0

for data in datas :
    title = data.select_one("span.subject_fixed")
    reply_count = data.select_one("span.rSymph05")
    link = data.select_one("a.list_subject")
    if title != None :
        index += 1
        print(index, title.get_text().strip(), [int(reply_count.get_text())])
        res_title = requests.get("https://davelee-fun.github.io/trial/board/"+link["href"])
        soup_title = BeautifulSoup(res_title.content, "html.parser")
        replies = soup_title.select("div.comment_content")
        for reply in replies :
            print("  ㄴ", reply.get_text().strip().replace(" ", "").replace("\n", "").replace("\t", ""))