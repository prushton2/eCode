import sys

charmap = __import__("charmap")
eCode = open(sys.argv[2], "w")
pyCode = open(sys.argv[1], "r")


program = ""
for i in pyCode.read():
    program += "e"*(charmap.charmap.index(i)+1)
    program += " "
eCode.write(program)

eCode.close()
pyCode.close()