def getWordValue(w):
    s = 0
    for ch in w:
        s = s + ord(ch)-64
    return(s)
    
f = open("words.txt", 'r')
lines = f.readlines()
f.close()
line = lines[0]
line = line[1:-1]

s = line.split("\",\"")

max = 20 * 26
l = []

val = 1
i = 1

while(val <= max):
    val = (i*(i+1))//2
    l.append(val)
    i = i+1

count = 0

for word in s:
    v = getWordValue(word)
    if v in l:
        count += 1

print(count)
