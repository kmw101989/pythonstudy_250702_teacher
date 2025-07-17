string = "10,11,12,13,14"
split_string = string.split(",")

for index, split_item in enumerate(split_string) :
    split_string[index] = int(split_item)
print(split_string)