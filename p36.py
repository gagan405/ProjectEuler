sum = 0

def isBinaryPalindrome(n):
    x = bin(int(n))
    if(x[2:] == x[::-1][:-2]):
        return(True)
    else:
        return(False)

def getPalindromes(s, lt_idx):
    global sum
    if(len(s) == 1):
        for i in range(1, 10):
            s = str(i)
            if(isBinaryPalindrome(s)):
                sum = sum + int(s)
        return    
    #is mid of the tring ?
    ll = 1
    if(len(s) > 2):
            ll = 0
    if((len(s) % 2 == 1) and (lt_idx == len(s)//2)):
        for i in range(ll, 10):
            s = s[0:lt_idx] + str(i) + s[lt_idx+1:]
            if(isBinaryPalindrome(s)):
                sum = sum + int(s)
        return
    if((len(s) % 2 == 0) and (lt_idx + 1 == len(s)//2)):
        for i in range(ll, 10):
            s = s[0:lt_idx] + str(i) + str(i) + s[lt_idx+2:]
            if(isBinaryPalindrome(s)):
                sum = sum + int(s)
        return
    
    if(lt_idx > 0):
        ll = 0
    else:
        ll = 1
        
    for i in range(ll, 10):
        s = s[0:lt_idx] + str(i) +  s[1+lt_idx:len(s)-1-lt_idx] + str(i) + s[len(s)-lt_idx:]
        getPalindromes(s, lt_idx+1)
        
    
getPalindromes("x",0)    
getPalindromes("xx",0)
getPalindromes("xxx",0)
getPalindromes("xxxx",0)
getPalindromes("xxxxx",0)
getPalindromes("xxxxxx",0)
print(sum)
