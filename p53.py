#nCr = (n-1)C(r-1) + (n-1)Cr
#nC(r-1) = nCr * r/n-r+1

limit = 1000000

def calc_n_r_v(n, r, v):
    n_c_r_1 = (v * r)//(n - r + 1)
    n_p_1_c_r = n_c_r_1 + v
    n_p_1_c_r_1 = (n_p_1_c_r * r)//(n+2-r)
    
    if(n_p_1_c_r_1 < limit):
        return (n+1,  r,  n_p_1_c_r)
    else:
        prevVal = n_p_1_c_r_1
        nextVal = limit + 1
        r = r-1
        n = n+1
        while(nextVal > limit):
            nextVal = (prevVal*r)//(n - r + 1)
            if(nextVal > limit):
                prevVal = nextVal
                r = r-1
        return (n, r, prevVal)
            
    

def countMoreThanLimit():
    n = 23
    r = 10
    v = 1144066
    count = n - 2*r + 1
    print("count : " + str(count))
    
    while(n < 100):
        n, r, v = calc_n_r_v(n, r, v)
        print(n, r, v)
        count += n - 2*r + 1
        
    print(count)
    
countMoreThanLimit()
        
