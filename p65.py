import sys
# a + b/c

def sumDigits(n):
    s = 0
    while n:
        s = s + n % 10
        n = n//10
    return s
    
def findNthFrac(n, a, b, c):
    if(n == 2):
        res = 2*c+b
        print(str(res) + '/' + str(c))
        print("Sum of digits of numerator : " + str(sumDigits(res)))
        return
    
    #n-2th term is the new a
    if((n%3 == 0) or ((n-1)%3 == 0)):
        new_a = 1

    elif((n+1)%3 == 0):
        new_a = 2*((n-2)//3)
        
    new_c = a*c +b
    new_b = c
    n = n-1
    return(findNthFrac(n, new_a,  new_b, new_c))
    

def findFrac(n):
    if(n == 1):
        print(2)
        return
    
    if (n%3 == 0):
        c = 2*(n//3)
        a = 1
        b = 1
        return(findNthFrac(n, a, b, c))
    else:
        if((n-1)%3 == 0):
            c = 1
            a = 2*((n-1)//3)
            b = 1
            return(findNthFrac(n, a, b, c))
        if((n+1)%3 == 0):
            if(n-1 == 1):
                a = 2
                b = 1
                c = 1
                return(findNthFrac(n, a, b, c))
            else:
                a = 1
                b = 1
                c = 1
                return(findNthFrac(n, a, b, c))

findFrac(int(sys.argv[1]))
