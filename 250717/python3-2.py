# 12
import re

pattern08 = re.compile("[^a-zA-Z0-9]")

pattern08.search("----30294----")

# 13
import re

pattern09 = re.compile("[가-힣]")

pattern09.search("김")

# 14
import re
pattern10 = re.compile("[a-z]+")

matched = pattern10.match("Dave")
print(matched)
searched = pattern10.search("Dave")
print(searched)

# 15
import re
# pattern11 = re.compile("[a-z]+")
pattern11 = re.compile("[a-zA-Z]+")
findalled = pattern11.findall("Game of Life in Python")
print(findalled)

# 16
import re

pattern12 = re.compile("[a-z]+")

finalled01 = pattern12.findall("GaME")

if len(finalled01) > 0 :
    print("정규표현식에 맞는 문자열이 존재함")
else :
    print("정규표현식에 맞는 문자열이 존재하지 않음")

# 17
import re

pattern13 = re.compile(":")

splited = pattern13.split("python:java")
print(splited)