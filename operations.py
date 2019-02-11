def op(instruction):
    keywords = instruction.strip().split()
    #map missing memory addresses
    if keywords[0] not in memory:
        memory[keywords[0]] = 0
    if keywords[4] not in memory:
        memory[keywords[4]] = 0

    #process the operation
    arg1 = int(keywords[2])
    if keywords[1] == "dec":
        arg1 = -arg1
    #jesus christ how horrifying
    if eval("memory[\"" + keywords[4] +"\"]" + keywords[5] + keywords[6]):
        memory[keywords[0]] += arg1
    return memory[keywords[0]]


with open("ops.txt") as f:
    lines = f.readlines()
memory = {}
maxVal = 0
for line in lines:
    temp = op(line)
    if temp > maxVal:
        maxVal = temp
index = max(memory, key=memory.get)
print(memory[index])
print(maxVal)
