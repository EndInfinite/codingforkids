def getMax(a, b, c):
    biggest = 0
    if a > biggest:
        biggest = a
        if b > a:
           biggest = b
           if c > b:
                biggest = c
        elif c > a:
            biggest = c 
    elif b > biggest: 
        biggest = b
        if c > b:
            biggest = c
    elif c > biggest:
        biggest = c
    return biggest

d = getMax(43, 45, 42)
print("the max number is: ", d)


def getMax2(a, b, c):
    biggest = a
    if b > biggest: 
        biggest = b
        if c > b:
            biggest = c
    elif c > biggest:
        biggest = c
    return biggest

d2 = getMax2(48, 48, 48)
print("the max number is: ", d2)


def getMax3(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c

d3 = getMax3(42, 41, 43)
print("the max number is: ", d3)


def getMax4(a, b, c):
    myList = [a, b, c]
    myList.sort()
    return myList[2]

d4 = getMax4(48, 46, 47)
print("the max number is: ", d4)