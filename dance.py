def spin(alphaList, offset):
    copy = alphaList[:]
    for i in range(len(alphaList)):
        alphaList[i] = copy[(i - offset)%16]
    return alphaList

def exchange(alphaList, posa, posb):
    copy = alphaList[:]
    alphaList[posa] = copy[posb]
    alphaList[posb] = copy[posa]
    return alphaList

def partner(alphaList, vala, valb):
    copy = alphaList[:]
    for posx in range(len(alphaList)):
        if alphaList[posx] == vala:
            break
    for posy in range(len(alphaList)):
        if alphaList[posy] == valb:
            break
    alphaList[posx] = valb
    alphaList[posy] = vala
    return alphaList

def dance(alphaList, ops):
    for op in ops:
        if op[0] == 's':
            alphaList = spin(alphaList, int(op[1:]))
        elif op[0] == 'x':
            alphaList = exchange(alphaList, int(op[1:].split('/')[0]), int(op[1:].split('/')[1]))
        elif op[0] == 'p':
            alphaList = partner(alphaList, op[1:].split('/')[0].strip(), op[1:].split('/')[1].strip())
    return alphaList

with open("dance.txt", "r") as f:
    ops = f.readline().split(",")

alphaList = [chr(i) for i in range(ord('a'), ord('p') +1)] #test is a to e, day is a to p
startList = alphaList[:]

alphaList = dance(alphaList, ops)
stepList  = alphaList[:]
steps = 1

while True:
    tempList = alphaList[:]
    alphaList = dance(alphaList, ops)
    if alphaList == stepList and tempList == startList: #obviously whatever the succession is, an identical step shows a cycle.
        break
    steps +=1

for x in range(1000000%steps):
    startList = dance(startList, ops)

print(''.join(startList))
