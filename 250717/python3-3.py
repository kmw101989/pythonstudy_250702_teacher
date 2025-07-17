import re

word = "801210 - 1011323"
pattern15 = re.compile("-")
subed = pattern15.sub("*", word)

print(subed)