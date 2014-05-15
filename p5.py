import sys

#LCM of first 20 numbers

num = 2520

for i in range(11,21):
    for j in range(1,i+1):
        if ((num*j)%i == 0):
            num = num*j
            break  
print(num)
