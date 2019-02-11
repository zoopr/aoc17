class Element:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def weigh(item):
    totalWeight = item.weight
    childrenBalance = int(-1)
    #find children's weight. recursively check their weight.
    for child in item.children:
        for piece in towerElements:
            if piece.name == child:
                if childrenBalance == -1:#initialize match for first child.
                    childrenBalance = weigh(piece)
                if weigh(piece) != childrenBalance:
                    print("IMBALANCE")
                    print(item.name)
                    print(str(childrenBalance) + " vs " + str(weigh(piece)))
                    break
                totalWeight += weigh(piece)
    return totalWeight

with open("tower.txt") as f:
    lines = f.readlines()

towerElements= list()

for line in lines:
    item = Element("", 0, [])
    left, dummy = line.split(" (", 1)
    dummy, right = dummy.split(")", 1)
    item.name = left[:]
    item.weight = int(dummy[:])
    if len(right)>3:
        right = right.split("> ", 1)
        for level in right[1].split(","):
            item.children.append(level[:].strip(" \n"))
    towerElements.append(item)

for piece in towerElements:
    if piece.name == "fbgguv":         #fbgguv is the bottom level, from part 1. zsasjr has an imbalance. jdxfsa is 5 units too heavy.
        print(weigh(piece)) #952
        for child in piece.children:
            for piece2 in towerElements:
                if piece2.name == child:
                    print(piece2.name)
                    print(weigh(piece2))
