import openpyxl
import re

work_book = openpyxl.load_workbook("data_kr.xlsx")
work_sheet = work_book.active

for each_row in work_sheet.rows :
    # print(each_row[1].value)
    print(re.sub("-[0-9]{7}", "-*******", each_row[1].value))