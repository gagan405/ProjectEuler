import math

phi = 1.6180339887
d = 999/math.log10(phi)

def calc(n):
    f = phi**n
    f = f/(5**(1/2)) + 1/2
    return(math.floor(f))
    
print("Near to the fib number : " + str(math.floor(d)))    

