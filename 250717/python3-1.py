# 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

res = urlopen("https://crawlingtest.netlify.app/")
soup = BeautifulSoup(res, "html.parser")

datas = soup.select("ul#dev_course_list > li.course")
for data in datas :
    print(re.sub("\[[0-9]+\]", "", data.get_text()).strip()) # escape sequence => \n \t
    # print(data.get_text().strip())

# 2
import openpyxl
import re

regex = re.compile(" [A-Za-z]+\.")

work_book = openpyxl.load_workbook("train.xlsx")
work_sheet = work_book.active

for each_row in work_sheet.rows :
    print(each_row[3].value)
    print(regex.findall(each_row[3].value))

# 3
import re

string = "(Dave)"
re.sub('[^A-Za-z0-9]', "", string)

# 4
import re

pattern = re.compile("D.A")

# pattern.search("DAA")
# pattern.search("DBA")
pattern.search("DCCA")
pattern.search("DA")
pattern.search("dOA DIA 0011")

# 5
import re

pattern01 = re.compile("D?A")

pattern01.search("A")
pattern01.search("DA")
pattern01.search("DDA")
pattern01.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA")

# 6
import re

pattern02 = re.compile("D*A")
pattern02.search("A")
pattern02.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA")

# 7
import re

pattern03 = re.compile("D+A")

pattern03.search("A")
pattern03.search("DA")
pattern03.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA")

# 8
import re

pattern04 = re.compile("A{2}D{1}A")

pattern04.search("AADA")
# pattern04.search("ADDA")
# pattern04.search("ADDDA")

# 9
import re

pattern05 = re.compile("AD{2,6}A")

pattern05.search("ADDA")
pattern05.search("ADDDDDDDA")

# 10
import re

pattern06 = re.compile("[abcdefgABCDEFG]")

pattern06.search("a1234")
pattern06.search("z1234")

# 11
import re

pattern07 = re.compile("[a-zA-Z0-9]")

pattern07.search("1234---")