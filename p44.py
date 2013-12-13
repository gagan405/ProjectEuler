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

for n in range(1, 2201):
    li.append((n*(3*n-1))//2)

for i in range(0, 2200):
    for j in range(i, 2200):
        if(isPentagonal(li[i] + li[j]) and isPentagonal(li[j] - li[i])):
            print("i : " + str(i) + " j : " + str(j) + " diff " + str(li[j] - li[i]))

mid = timeit.default_timer()
print(mid - start)

flag = False
n = 1
diff = 0

while(flag != True):
    m = 1
    while(m <= n):
        diff = (n-m)*(3*m+3*n-1) // 2
        if(isPentagonal(diff)): 
            if isPentagonal((3*m*m-m+n*(3*n-1))//2):
                flag = True;
                break
        m += 1
    n += 1
    
print(diff)
stop = timeit.default_timer()

print(stop - mid)
