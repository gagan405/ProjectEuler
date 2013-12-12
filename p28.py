import sys

diff = 2

num = 3
sum = 1
count = 1

while(num <= 1001**2): 
    sum = sum + num
    count = count + 1
    num = num + diff
    if count == 4:
        diff = diff + 2
        count = 0
print(sum)
    
