# fibonachci number module

def getFibo(number):
    a, b = 0, 1
    while b < number:
        print(b, end=" ")
        olda = a
        a = b
        b = olda + b
    print()


def getFibo2(number):
    result = []
    a, b = 0, 1
    while b<number:
        result.append(b)
        olda = a
        a = b
        b = olda + b
    return result

getFibo(100)

myFibo = getFibo2(100)
print("this is the result by calling the myFibo2() function: {0}".format(myFibo))
