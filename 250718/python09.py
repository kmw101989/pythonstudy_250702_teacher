import requests
import openpyxl
from bs4 import BeautifulSoup
from openpyxl.styles import Alignment, Font

wrap_alignment = Alignment(wrap_text=True)
bold_font = Font(bold=True)
header_font = Font(bold=True, size=14)
normal_font = Font(bold=False)

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.title = "게시글"

header = ["No", "게시글 제목", "댓글수"]
excel_sheet.append(header)

for cell in excel_sheet[1] :
    cell.font = header_font

excel_sheet.column_dimensions["A"].width = 20
excel_sheet.column_dimensions["B"].width = 80
excel_sheet.column_dimensions["C"].width = 80

res = requests.get("https://davelee-fun.github.io/trial/board/news.html")
soup = BeautifulSoup(res.content, "html.parser")

datas = soup.select("div.list_item")
index = 0
row = 2

for data in datas :
    title = data.select_one("span.subject_fixed")
    reply_count = data.select_one("span.rSymph05")
    link = data.select_one("a.list_subject")
    if title != None :
        index += 1
        # print(index, title.get_text().strip(), [int(reply_count.get_text())])
        link_url = "https://davelee-fun.github.io/trial/board/"+link["href"]
        data1 = [index, title.get_text().strip(), "[" + reply_count.get_text() + "]"]
        excel_sheet.append(data1)
        excel_sheet.cell(row = row, column = 2).hyperlink = link_url
        
        for cell in excel_sheet[row] :
            cell.font = bold_font
        row += 1
        res_title = requests.get("https://davelee-fun.github.io/trial/board/"+link["href"])
        soup_title = BeautifulSoup(res_title.content, "html.parser")
        replies = soup_title.select("div.comment_content")
        for reply in replies :
            data2 = ["", "", reply.get_text().strip().replace(" ", "").replace("\n", "").replace("\t", "")]
            # print("  ㄴ", reply.get_text().strip().replace(" ", "").replace("\n", "").replace("\t", ""))
            excel_sheet.append(data2)
            for cell in excel_sheet[row] :
                cell.font = normal_font
                cell.alignment = wrap_alignment
            row += 1
excel_file.save("mysite.xlsx")
excel_file.close()

print("✅ mysite.xlsx 저장완료!!!")