import sys
import math

li = [2,3,5,7]
lst = 7

def getPrimesTillN(n):
    global lst
    last = lst

    if n == last:
        return len(li) #nothing to do
    elif last > n:
        i = 0
        while(li[i] <= n):
            i+=1    
        return i
    else: #fill li with primes till n
        i = 1
        while(last + i <= n ):
            j = 0
            k = len(li)
            while(j < k):
                if ((last+i)%li[j] == 0):
                    break
                else:
                    j+=1
                if (j == (k-1)):
                    #its a prime
                    li.append(last+i)            
            i+=1
        last = n
        lst = n    
        return len(li)

def getNumOfFactors(val,x):
    num = 1
    if x == 0:
        x = 1
    i = 0
    while(i < x):
        p = 1
        while(val%(li[i]**p) == 0):
            p+=1
        num *= p
        i+=1
    return num

if __name__ == "__main__":
    numOfFactors = 1

    idx = int(sys.argv[1])
    val = (idx*(idx+1))/2
    num = math.floor(val/2)
    x = getPrimesTillN(num)
   
    print(getNumOfFactors(val,x))
    
    
