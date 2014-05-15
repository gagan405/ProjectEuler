import sys

#Dijkstra's method to find fibonacci numbers in less iterations

fibs = {0: 0, 1: 1}
li = []
def fib(n):
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
        return fibs[n]

if __name__ == "__main__":
    i = 1
    f = 1
    sum = 0
    while(f < 4000000):
        f = fib(i)
        if (f%2 == 0) :
            if (f < 4000000) :
                sum = sum + f
        i = i+1

    print(sum)
