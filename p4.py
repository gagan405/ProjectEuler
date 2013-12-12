import sys

#Get the largest palindrome by multiplying 2 3-digit numbers
#There is a better way to do this with less loops

largest = 0
n1 = 0
n2 = 0

for i in range (100,1000):
    for j in range (i, 1000):
        mul = i*j
        if (str(mul) == str(mul)[::-1]) :
            if (largest < mul):
                largest = mul;
                n1 = i
                n2 = j
            
print(n1, n2, largest)
