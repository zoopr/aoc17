def trail(path, pos, direction, crumbs):
    y, x = pos
    dy, dx = direction
    validSteps = ["|", "-"] #this is required for the routine check and more importantly for the direction change.
    nextStep = [y+dy, x+dx]
    if path[nextStep[0]][nextStep[1]] not in validSteps: #technically this validates the crossing, valid step of an overlaying direction.
        if path[nextStep[0]][nextStep[1]] == "+":        #but the check's purpose is to look for the following two types of characters, so there's no technical difference.
            print("met +, new direction")
            if abs(dy) == 1:
                test1 = [nextStep[0],nextStep[1] - 1]         #MAKE SURE THE INPUT IS CORRECTLY PADDED WITH WHITESPACE ON THE 201x201 GRID. I know I didn't. Fuck Atom.
                if path[test1[0]][test1[1]] == validSteps[1]: #RE: comment lines 6-7;however in these two tile checks, which one we match is important.
                    direction = [0, -1]                       #there could be back to back parallel paths, but we want to change direction.
                else:                                         #there is no safeguard for such a case covering my actual following tile but thankfully that doesn't happen in my input.
                    direction = [0, 1]                        #this also fails if there's a + to + u-turn.
            else:
                test1 = [nextStep[0] - 1, nextStep[1]]
                if path[test1[0]][test1[1]] == validSteps[0]:
                    direction = [-1, 0]
                else:
                    direction = [1,0]
        if path[nextStep[0]][nextStep[1]].isalpha(): #obviously this can't cover a +, so it's otherwise treated as a valid step(no direction evaluation)
            crumbs.append(path[nextStep[0]][nextStep[1]])

    return direction #this lax check will let the position pointer walk off into whitespace. I've designed the container loop to exit when this happens.

with open("path.txt") as f:
    path = f.readlines() #make sure you don't strip() as we need the precise grid position and the padding.


pos = [0, 13] #not sure if other inputs have different starting positions. this is the only tile in my outer ring anyway.
direction = [1, 0] #these two pieces of data were handpicked but it's easy enough to automate my observation above.
crumbs = []
steps=0

while path[pos[0]][pos[1]].isspace() == False:
    print(pos)
    steps+=1
    newpos = [pos[0] + direction[0], pos[1] + direction[1]] #save the safe step forward
    direction = trail(path, pos, direction, crumbs) #calculate the direction from that step on
    pos = newpos #move onto the previous step's safe spot, with the new direction ready for this step.
print (''.join(crumbs))
print(steps)
