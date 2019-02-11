from queue import Queue

with open("14.out") as f:
    lines = [line.strip() for line in f.readlines()]
ones = {(i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == '1'}

groups = 0
queue = Queue()
while ones:
    groups += 1
    item = ones.pop()
    queue.put(item)
    while queue.empty() == False:
        i, j = queue.get()
        for coords in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
            if coords in ones:
                ones.remove(coords)
                queue.put(coords)
print(groups)
