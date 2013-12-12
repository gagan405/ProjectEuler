import sys
li = []

def nextStep(n):
    count = 1

    if len(li) > n:
        return(li[n-1])

    if n == 1:
        return count
    elif n%2 == 0:
        return (count + nextStep(int(n/2)))
    else:
        return (count + nextStep((3*n)+1))
    

if __name__=="__main__":
    z = 4 
    num = 8
    for x in range(1,1000000):
        y = nextStep(x)
        li.append(y)
        if y > z:
            z = y
            num = x
    print(num, z)
