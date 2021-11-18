charmap = __import__("charmap")
eCode = open("eCode.e", "w")
pyCode = open("eCode.py", "r").read()

program = ""
for i in pyCode:
    program += "e"*(charmap.charmap.index(i)+1)
    program += " "
eCode.write(program)