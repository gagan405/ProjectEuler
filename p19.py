import sys


def isLeapYr(n):
    if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
        return 1
    else: return 0

yr = 1900
mon = 12
day = 6
week = ["sun", "mon", "tue","wed", "thu", "fri", "sat" ]

li = [31,28,31,30,31,30,31,31,30,31,30,31]

if __name__ == "__main__":
    count = 0
    while (yr < 2001):
        if mon == 2:
            day += li[1] + isLeapYr(yr)
        else:
            day += li[mon-1]

        day = day%7

        print(week[day])

        if day == 0:
            count += 1

        mon +=1
        if mon == 13:
            print (yr)
            mon = 1
            yr +=1
            if yr == 2001 and day == 0:
                count = count-1

print(count)
