
def iterate(arr):
    maxNum = max(arr)
    indexMax = arr.index(max(arr))

    arr[indexMax] = 0
    for i in arr:
        i+= int(maxNum/len(arr))
    for i in range(indexMax+1, indexMax + (maxNum%len(arr)) + 1):
        arr[i%len(arr)] += 1





with open("banks.txt") as f:
    line = f.readline()

banks = [int(x) for x in line.split()]
states = []
steps = 0

while True:
    if banks in states:
        print(steps - states.index(banks) )
        break
    states.append(banks[:])
    iterate(banks)
    steps+=1
print(steps)
