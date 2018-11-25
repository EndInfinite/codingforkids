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

print(largeNumber)

for i in range(len(number)-4):
    a = int(number[i])
    b = int(number[i+1])
    c = int(number[i+2])
    d = int(number[i+3])
    product = a*b*c*d
    if a*b*c*d == largeNumber:
        theList.append(a)
        theList.append(b)
        theList.append(c)
        theList.append(d)

x = [theList[0],theList[1],theList[2],theList[3]]
y = [theList[4],theList[5],theList[6],theList[7]]
        
print(x)
print(y)
