def getRecurringLength(n):
    l = [1]
    r = 1
    while(True):
        q = 10*r
        r = q % n
        #if r is in the list, break, else continue
        if(r == 0):
            return(0)
        try:
            i = l.index(r)
            return(len(l)-i)
        except ValueError:
            l.append(r)

max = 0
max_num = 0

for i in range(2, 1001):
    l = getRecurringLength(i)
    if(l > max):
        max = l
        max_num = i

print("Max recurting length is " + str(max) + " of number " + str(max_num))
