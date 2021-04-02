phrase = "The right format"
strlen = len(phrase)
pad = 42 - strlen
newstr = ""
while pad>0:
    newstr += "-"
    pad = pad -1
newstr += "".join(phrase)
print(newstr, end="")
