import sys

li = [2,3,5,7]

def getNthPrime(n):
    if (n <= len(li)):
        return li[n-1]
    i = 0
    num = li[len(li)-1]+1

    if num%2 == 0:
        num = num + 1

    while (len(li) < n):
        while (li[i] * li[i] <= num):
            if num % li[i] == 0 :
                num += 2
                i = 0
                continue
            else :
                i += 1
        li.append(num)
        num = num + 2
        i = 0

    return li[n-1]

if __name__ == "__main__":
    sum = 0
    n = 1
    i = 1
    while (n < 2000000):
        n = getNthPrime(i)
        i += 1
        if n < 2000000 :
            sum += n

    print(sum)
