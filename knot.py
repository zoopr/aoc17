def op(skip, index, rope, ops):
    maxpos = ops[skip%len(ops)]
    for i in range(int(maxpos/2)):
        placeholder = rope[(index + i)%arrSize]
        rope[(index + i)%arrSize] = rope[(index + maxpos - 1 - i)%arrSize]
        rope[(index + maxpos - 1 - i)%arrSize] = placeholder
    return (index + maxpos + skip)%arrSize
def denseHash(arr): #arr length is hardcoded despite my attempts at tidier stuff in p1. cba.
    index = 0
    hashSum = []
    for block in range(16):
        hashSum.append(arr[16*block])
        #print(hashSum)
        for i in range(block*16+1, block*16+16):
            hashSum[block] = hashSum[block] ^ arr[i]
    return (['{:x}'.format(hashBlock) for hashBlock in hashSum])


ops = [ord(x) for x in "106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118"] #p1: int(x) for x in ....split(',')
ops.extend([17, 31, 73, 47, 23])


arrSize = 256 #we generate and modulo the array with this
index = 0 #this is updated each op
passes = 64 #how many times do we go through the instruction queue

rope = [i for i in range(arrSize)]


for skip in range(len(ops) * passes): #skip is just the move counter.
    index = op(skip, index, rope, ops)

finalHash = denseHash(rope)
print (finalHash)
