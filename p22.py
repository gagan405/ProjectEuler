import sys

str = open("names.txt").readline()
str = str.lower()
str = str.strip('\"')
li = str.split('\",\"')


li.sort()
sum = 0

for i, st in enumerate(li):
#    print (i, st)
    val = 0
    for j in range(0, len(st)):
        val += ord(st[j])-ord('a') + 1
    val *= i+1
    sum += val
 
print (sum)
