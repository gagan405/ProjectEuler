import math
import timeit

def is_perfect_square(n):
    nsqrt = math.sqrt(n)
    return nsqrt == math.trunc(nsqrt)

def isPentagonal(n):
    if(is_perfect_square(24*n+1)):
        x = math.sqrt(24*n+1)+1
        if(x%6 == 0):
            return True
        else:
            return False
    return False

li = []
start = timeit.default_timer()

n = 144

while(True):
    hNext = n*(2*n-1)
    if(isPentagonal(hNext)):
        print(hNext)
        break
    n += 1

stop = timeit.default_timer()
print(stop - start)
