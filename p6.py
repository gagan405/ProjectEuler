import sys

def prob_1(n):
    """ Calculate the differenece between sum of squares all the numbers below the input number and square of their sum """
    return ( (int((n*(n+1))/2)**2) - int((n*(n+1)*((2*n)+1))/6))  

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(prob_1.__doc__)
    else:
        print(prob_1(n=int(sys.argv[1])))
