def getCommonList(list1, list2):
    myList = []
    for a in list1:
        if a in list2 and a not in myList:  #we can also try to use set() to remove the duplications
            myList.append(a)
    return myList


testList1 = [1, 1, 3, 5, 9, 20, 34, 55, 73, 98]
testList2 = [1, 2, 3, 4, 7, 9, 34, 35, 38]

commonList = getCommonList(testList1, testList2)
print(commonList)