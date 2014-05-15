sum = 0
limit = 1000000000

def getNextVal(a, b):
    return ((2*a + 3*b), (a + 2*b))
    
def getTriangles():
    global sum
    x = 2
    y = 1
#    a = x**2 + y**2
#    b = 2*(x**2-y**2)
    
    
    while(True):
    
        a3 = 2*x - 1
        area3 = y*(x-2)    
    
        if(a3 > limit):
            break 
    
        if (a3 > 0 and area3 > 0 and
            a3 % 3 == 0 and area3 % 3 == 0):
            a = a3 // 3;
            sum += 3 * a + 1;
    
        a3 = 2 * x + 1;
        area3 = y * (x + 2);
 
        if (a3 > 0 and  area3 > 0 and
            a3 % 3 == 0 and  area3 % 3 == 0):
 
            a = a3 // 3;
            sum += 3 * a - 1;

        x, y = getNextVal(x, y)
    
getTriangles()
print("Sum of perimeters : ",  str(sum))
