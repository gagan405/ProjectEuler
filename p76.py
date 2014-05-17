import sys

def countCombinations(Number, Minimal):
	temp = 1
	if (Number<=1):
		return 1
  	for i in range(1, Number//2 +1):
		if(i>= Minimal):
			temp += countCombinations(Number-i, i)
   	return temp

print(countCombinations(6, 1) - 1)

##NEED TO DO IT IN DYNAMIC PROG