for i in range(1, 10):
    for j in range(1, 10):
        num = i*10 + j
        for k in range(i, 10):
            for l in range(1, 10):
                den = k*10+l
                if(num == den):
                    continue
                if(i == k):
                    if(num/den == j/l):
                        print(str(num) + "/" + str(den))
                elif(i == l):
                    if(num/den == j/k):
                        print(str(num) + "/" + str(den))
                elif(j == k):
                    if(num/den == i/l):
                        print(str(num) + "/" + str(den))
                elif(j == l):
                    if(num/den == i/k):
                        print(str(num) + "/" + str(den))

