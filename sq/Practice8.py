a =[1,1,3,5,9,20,34,55,73,98]
b = [1,2,3,4,7,9,34,35.38]

myList = []

for item in b:
    if item in a:
        myList.append(item)
return myList

print(myList)