

def getNum(n, lim):
    
    while(n < lim):
        l1 = list(str(n))
        l1.sort()
        l2 = list(str(n*2))
        l2.sort()
        
        if(l1 != l2):
            n += 1
            continue
    
        l3 = list(str(n*3))
        l3.sort()
        if(l2 != l3):
            n += 1
            continue
        l4 = list(str(n*4))
        l4.sort()
        if(l3 != l4):
            n += 1
            continue
    
        l5 = list(str(n*5))
        l5.sort()
        if(l4 != l5):
            n += 1
            continue
    
        l6 = list(str(n*6))
        l6.sort()
        if(l5 != l6):
            n += 1
            continue
    
        print("Found " + str(n))
        return(True)
    
    return(False)

n = 101
lim = 166

while(getNum(n,  lim) != True):
    n = (n-1)*10 + 1
    lim = lim*10 + 6
    print(n, lim)
