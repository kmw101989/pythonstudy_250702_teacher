# 1
data = "Dave David"
data.count("Dave")
data.count("D")

# 2
string = "Dave ID is dave"
string.index("D")
string.index("d")
# string.index("x")

# 3
string01 = "Dave ID is dave"
string01.find("x")
string01.find("a")

if string01.find("x") == -1 :
    print("x는 string01 문자열 객체 안에 없습니다.")

# 4
string02 = "12345"
comma = ","

comma.join(string02)

# 5
data01 = " Dave "
data01.strip()

data02 = "       Dave02 "
data02.strip()

data03 = "       Dave03 "
data03.lstrip()

data04 = "       Dave04 "
data04.rstrip()

# 6
string03 = "       9999999999999999(Dave)888888888888     "
string03.strip(" 98()")

string04 = "Dave ID is dave"
string04.upper()

string05 = "Dave ID is dave"
string05.lower()

string06 = "Dave goes to Korea"
string06.split()[3]
string06.split(" ")

string07 = "Dave/goes/to/Korea"
string07.split("/")