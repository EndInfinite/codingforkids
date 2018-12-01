a =[1,1,3,5,9,20,34,55,73,98]
b = [1,2,3,3,4,7,9,34,35,38]

def myNumbers(a,b):
    myList = []
    for item in b:
        if item in a:
            if item not in myList:
                myList.append(item)
    return myList

myAnswer = myNumbers(a,b)
print(myAnswer)
