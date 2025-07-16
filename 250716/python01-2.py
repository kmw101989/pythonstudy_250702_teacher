import requests
import pprint
import openpyxl

client_id = "XDGy5Y0uSe8v0dIAc7Z4"
client_secret = "MUpLnN9M0I"
start, num = 1, 0

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions["B"].width = 100
excel_sheet.column_dimensions["C"].width = 100
excel_sheet.append(["No", "제목", "링크"])

for index in range(10) :
    start_number = start + (index * 100)
    naver_open_api = "https://openapi.naver.com/v1/search/shop.json?query=무신사&display=100&start=" + str(start_number)
    header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    res = requests.get(naver_open_api, headers=header_params)
    
    if res.status_code == 200 :
        data = res.json()
        # pprint.pprint(data)
        # print(data["items"][0]["title"])
        for item in data["items"] :
            num += 1
            excel_sheet.append([num, item["title"], item["link"]])
            print(num, item["title"], item["link"])
    else :
        print("Error Code: ", res.status_code)

excel_file.save("shopping_with_무신사.xlsx")
excel_file.close()