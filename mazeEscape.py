

#input initial tile set
with open("inputMaze.txt") as f:
    lines = f.readlines()

tiles = [int(x.strip('\n')) for x in lines]

#set the actual game
steps = 0
index = 0
while index < len(tiles):
    x = tiles[index]
    if x >=3:
        tiles[index] -= 1
    else:
        tiles[index] += 1
    index += x
    steps += 1

print(steps)
