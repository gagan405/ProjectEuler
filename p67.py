import sys

file = open("triangle.txt")
li = []

for line in file:
    tmp = (line.rstrip()).split(" ")
    tmp = [int(x) for x in tmp]
    li.append(tmp)

#for i in range (0,len(li)):
#    print(li[i])

for i in reversed(range(len(li))):
    if i==0:
        break
    for j in range(1,len(li[i])):
        if li[i][j] < li[i][j-1] :
            li[i-1][j-1] += li[i][j-1]
        else:
            li[i-1][j-1] += li[i][j]
    del li[i]
#    for i in range (0,len(li)):
#        print(li[i])
    
print(li[0][0])
