import sys
import math

#Sum of all the digits of 100! 

strn = str(math.factorial(10))
sum = 0

for c in strn:
    sum = sum + int(c)

print(sum)
