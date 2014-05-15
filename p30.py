i = 2
sum = 0

def sumOfPowers(n):
    sum = 0
    s = str(n)
    for c in s:
        sum += int(c)**5
    return sum == n

while(i < 355000):
    if(sumOfPowers(i)):
        sum += i
        print("N = " + str(i))
    i += 1
print(sum)
