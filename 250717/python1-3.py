
import subprocess
import xml.etree.ElementTree as ET
import requests
import openpyxl
from openpyxl.drawing.image import Image as ExcelImage
from io import BytesIO

url = "https://apis.data.go.kr/B551011/GoCamping/basedList?numOfRows=50&pageNo=1&MobileOS=ETC&MobileApp=camping&serviceKey=RGzR0pEvB08eGZWqjj0mYonhz1%2Bkj6rzw2MBbGWGY99AroOuOwtjHo8LOJESQ8Q6jyV9jhaIcfndl%2BG6pi4v0A%3D%3D&_type=xml"

result = subprocess.run(["curl", "-k", url], capture_output=True, text=True, encoding="utf-8")
root = ET.fromstring(result.stdout)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "캠핑장정보"
ws.append(["아이디", "캠핑장명", "이미지", "지역", "주소", "홈페이지"])

items = root.findall(".//item")
row = 2

for item in items :
    contentId = item.findtext("contentId", default="")
    facltNm = item.findtext("facltNm", default="")
    firstImageUrl = item.findtext("firstImageUrl", default="")
    doNm = item.findtext("doNm", default="")
    addr1 = item.findtext("addr1", default="")
    homepage = item.findtext("homepage", default="")

    ws.append([contentId, facltNm, "", doNm, addr1, homepage])

    if firstImageUrl :
        try :
            img_data = requests.get(firstImageUrl, timeout=10).content
            img_file = BytesIO(img_data)
            img = ExcelImage(img_file)
            img.width = 100
            img.height = 75
            ws.add_image(img, f"C{row}")
            ws.row_dimensions[row].height = 50
        except Exception as e :
            print(f"[경고] 이미지 다운로드 실패 : {firstImageUrl} -> {e}")
    row += 1

ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 20
ws.column_dimensions["D"].width = 15
ws.column_dimensions["E"].width = 50
ws.column_dimensions["F"].width = 50

wb.save("camping_info_1.xlsx")
print("✅ camping_info_1.xlsx 파일저장 완료!")