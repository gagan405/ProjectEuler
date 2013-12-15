#algo taken from : http://www.shaunspiller.com/happynumbers

count = 0

s1 = set([1, 10, 13, 31, 44, 32, 23])
s89 = set([85, 89, 98, 58, 145, 541, 415, 154, 514, 42, 24, 20, 4, 40, 2, 16, 61, 37, 73])

d1 = [0]*(1*9*9 + 1)
d2 = [0]*(2*9*9 + 1)
d3 = [0]*(3*9*9 + 1)
d4 = [0]*(4*9*9 + 1)
d5 = [0]*(5*9*9 + 1)
d6 = [0]*(6*9*9 + 1)
d7 = [0]*(7*9*9 + 1)


def sumOfDigSq(n):
    s = 0
    for c in str(n):
        s += int(c)**2
    return s


def isHappy(n):
    global s1
    global s89
    
    if(n == 0):
        return False
    if n in s1:
        return True
    if n in s89:
        return False
    
    l = []
    l.append(n)
    t = n
    while(True):
        t = sumOfDigSq(t)
        if t in s1:
            s1 |= set(l)
            return True
        if t in s89:
            s89 |=set(l)
            return False
        l.append(t)

for i in range(0, 10):
    d1[i**2] = 1
    
for i in range(0, 1*9*9+1):
   for d in range(0, 10):
        d2[i + d**2] += d1[i]
        
for i in range(0, 2*9*9+1):
   for d in range(0, 10):
        d3[i + d**2] += d2[i]

for i in range(0, 3*9*9+1):
   for d in range(0, 10):
        d4[i + d**2] += d3[i]

for i in range(0, 4*9*9+1):
   for d in range(0, 10):
        d5[i + d**2] += d4[i]

for i in range(0, 5*9*9+1):
   for d in range(0, 10):
        d6[i + d**2] += d5[i]

for i in range(0, 6*9*9+1):
   for d in range(0, 10):
        d7[i + d**2] += d6[i]

#for i in range(0,  7*9*9+1):
#    if (d7[i] != 0):
#        if(isHappy(i)):
#            count += d7[i]

for i in range(0,  7*9*9+1):
    if (d7[i] != 0):
        if(isHappy(i)):
            count += d7[i]
 
print(count)
#print(9999999 - count)
