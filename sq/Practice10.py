number = "7316717653133062491922511967442657474235534912493496353520312774506326239578318016944807958478851843"

largeNumber = 0
theList = []
for i in range(len(number)-4):
    a = int(number[i])
    b = int(number[i+1])
    c = int(number[i+2])
    d = int(number[i+3])
    product = a*b*c*d
    if product > largeNumber:
        largeNumber = product
    if a*b*c*d == largeNumber:
        theList = [a,b,c,d]
    
print(largeNumber)
print(theList)




