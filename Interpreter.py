charmap = __import__("charmap") 
eCode = open("eCode.e", "r")
codeOutput = open("codeOutput.py", "w")
eCode = eCode.read()

eCode = eCode.split(" ") 
program = ""

for i in eCode:
    program += charmap.charmap[len(i)-1]
program = program[0:-1] #For some reason it appends the last character in the charmap to the code, this removes it

codeOutput.write(program)
codeOutput.close()
codeToRun = __import__("codeOutput")
codeToRun