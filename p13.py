import sys
import fileinput

#sum of 50 100-digit numbers

sum = 0

for num in fileinput.input("p13.txt"):
    sum = sum + int(num)

print(sum)


