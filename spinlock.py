spinlock = [0, 1]
index = 1
stepLength = 349 #test is 3, day was 349

for steps in range(2, 50000001): #iterations are 2, 2018 for part 1; 2, 50000001 for p2
    index = (index + stepLength)%steps +1
    #spinlock = spinlock[:index] + [steps] + spinlock[index:]#part1. DISABLE FOR PART2
    if index == 1: #part2
        spinlock[1] = steps
print(spinlock[1]) #index+1 for part1, 1 for part2
