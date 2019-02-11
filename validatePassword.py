def anagrams(s1, s2):
    def sort(s):
        return sorted(s.lower())
    return sort(s1) == sort(s2)

def validate(line):
    w = line.strip("\n").split()
    for word in w:
        if w.count(word) > 1:
            return 0

        for word2 in w: #part 2
            if word2 != word and anagrams(word, word2):
                return 0
            
    return 1


lines = []
count = 0

with open("inputText.txt") as f:
    lines = f.readlines()

for x in lines:
    count += validate(x)

print(count)
