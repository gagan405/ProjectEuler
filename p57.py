count = 0

n = 1
nr  = 3
dr = 2

while(n < 1000):
    n_dr = nr + dr
    n_nr = nr + dr*2
    nr = n_nr
    dr = n_dr
    n += 1
    if(len(str(nr)) > len(str(dr))):
        count += 1

print(count)
        
