import sys

def prob_1(n):
    """ Calculate the sum of all the numbers below the input number which are multiples of 3 or 5 """
    return ( int(3*(int((n-1)/3)*(int((n-1)/3)+1))/2) + int(5*(int((n-1)/5)*(int((n-1)/5)+1))/2) - int(15*(int((n-1)/15)*(int((n-1)/15)+1))/2)  )

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(prob_1.__doc__)
    else:
        print(prob_1(n=int(sys.argv[1])))
    
    
    
