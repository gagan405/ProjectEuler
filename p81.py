import sys

matrix = [[0 for x in xrange(80)] for x in xrange(80)]

with open("/home/gbm/Code/Project Euler/p81.txt") as f:
    content = f.readlines()
    i = 0
    for line in content:
    	nums = line.strip('\n\r').split(',')
    	j = 0
    	for n in nums:
    		matrix[i][j] = int(n)
    		j += 1
    	i += 1

#print(matrix)


def getNewVal(i,j):
	if(j == 0):
		return matrix[i-1][j] + matrix[i][j]
	elif (i == 0):
		return matrix[i][j-1] + matrix[i][j]
	else:
		return min(matrix[i-1][j] + matrix[i][j], matrix[i][j-1] + matrix[i][j] )

def printMatrix():
    for i in range(0, 5):
        print(matrix[i])

i = 0
j = 0

n = 80 #size of each dim
m = 2*n - 1 # move along the diagonals -- num of diagonals

for x in range(1,m):
	i = (n-1) if x >= (n-1) else x
	j = 0 if x <= (n-1) else (x - n + 1) 
#	printMatrix()
#	print()
	while(True):
		matrix[i][j] = getNewVal(i,j)
		i -= 1
		j += 1
		if((i < 0) or (j > n-1)):
			break
print(matrix[n-1][n-1])	
