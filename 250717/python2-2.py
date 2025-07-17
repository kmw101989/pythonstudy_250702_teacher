string08 = "Dave goes to Korea"
string08.replace("Dave", "David")

string09 = "(David)"
string09.replace("(", "")

string10 = "(David)"
string10.replace("()", "")

string11 = "(David)"
# string12 = string11.replace("(", "")
# string12.replace(")", "")

# Method Chaining
string13 = string11.replace("(", "").replace(")", "")
string13