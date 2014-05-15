import sys

def isPalindrom(n):
	return str(n)[::-1] == str(n)

def isLychrel(n):
	for x in range(1,51):
		if(isPalindrom(n + int(str(n)[::-1]))):
			return False
		n += int(str(n)[::-1])
	return True

count = 0

for x in range(197,10001):
	if(isLychrel(x)):
		count += 1
print(count)
