

with open("matrix.txt") as f:
    lines = f.readlines()

arrsum = 0
for line in lines:
    items = [int(x) for x in line.strip().split()]
    for item1 in items:
        for item2 in items:
            if item2%item1 == 0 and item2 != item1:
                arrsum += item2/item1
                print(item1)
                print(item2)
print (arrsum)
