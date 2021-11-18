import sys
charmap = __import__("charmap") 
eCodeFile = open(sys.argv[1], "r")
codeOutput = open("codeOutput.py", "w")
eCode = eCodeFile.read()

eCode = eCode.split(" ") 
program = ""

for i in eCode:
    program += charmap.charmap[len(i)-1]
program = program[0:-1] #For some reason it appends the last character in the charmap to the code, this removes it

codeOutput.write(program)
codeOutput.close()
eCodeFile.close()
codeToRun = __import__("codeOutput")
codeToRun