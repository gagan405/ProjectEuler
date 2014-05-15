sum = 0

def check_div(idx, na,  li):
    global sum
    
    n_list = [i for i in range(0, 10) if i not in na]
    if(idx == 0):
            na.remove(0)
       
    for i in n_list:
        li[idx] = i
    
        if(idx == 3):
            x = int(''.join(str(y) for y in li[1:4]))
            if(x%2 != 0):
                continue
        if(idx == 4):
            x = int(''.join(str(y) for y in li[2:5]))
            if(x%3 != 0):
                continue
        if(idx == 5):
            x = int(''.join(str(y) for y in li[3:6]))
            if(x%5 != 0):
                continue
        if(idx == 6):
            x = int(''.join(str(y) for y in li[4:7]))
            if(x%7 != 0):
                continue
        if(idx == 7):
            x = int(''.join(str(y) for y in li[5:8]))
            if(x%11 != 0):
                continue
        if(idx == 8):
            x = int(''.join(str(y) for y in li[6:9]))
            if(x%13 != 0):
                continue
        if(idx == 9):
            x = int(''.join(str(y) for y in li[7:10]))
            if(x%17 != 0):
                continue
            else:
                n = int(''.join(str(y) for y in li[0:10]))
                print(n)
                sum += n
                continue
                
        na.append(i)
        check_div(idx+1,  na,  li)
        na.remove(i)
    return    
        
check_div(0, [0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print("sum is : " + str(sum))
