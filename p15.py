import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def pathForGrid(n):
    return int((factorial(2*n))/(factorial(n)**2))

if __name__ == "__main__":
    print(pathForGrid(int(sys.argv[1])))
