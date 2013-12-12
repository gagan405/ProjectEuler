import sys

s=0
for x in range(1,1000):
    s += (x**x)%(10**10)
print(s%(10**10))
