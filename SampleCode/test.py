"""
a = 12
b = 11
c = 11

myBig = a
if a >= myBig:
    myBig = a

if b >= myBig:
    myBig = b

if c >= myBig:
    myBig = c

print(myBig)
"""


a = [1, 3, 3, 5, 6]
b = [1, 2, 3]

def myFunction(a, b):

    myList = []

    for item in b:
        if item in a:
            myList.append(item)
    return myList

myResult = myFunction(a, b)
print(myResult)










