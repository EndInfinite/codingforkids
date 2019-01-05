'''A module to demostrate exception handling'''

def convertToInt(s):
    '''convert a given value s to an integer'''
    x = int(s)
    print("conversion is successful, the converted value is:", x)
    return x


def convertToInt2(s):
    '''convert a given value s to an integer'''
    try:
        x = int(s)
        print("conversion is successful, the converted value is:", x)
        return x
    except ValueError:
        print("conversion failed, unable to convert '{0}' to an integer.".format(s))
        return -1

def convertToInt3(s):
    '''convert a given value s to an integer'''
    try:
        x = int(s)
        print("conversion is successful, the converted value is:", x)
        return x
    except ValueError:
        print("conversion failed due to ValueError, unable to convert '{0}' to an integer.".format(s))
        return -1
    except TypeError:
        print("conversion failed due to TypeError, unable to convert '{0}' to an integer.".format(s))
        return -1

def convertToInt4(s):
    '''convert the values s to an integer'''
    try:
        x = int(s)
        print("conversion is successful, the converted value is:", x)
        return x
    except ValueError as e:
        print("conversion failed due to ValueError, unable to convert '{0}' to an integer. The exception message is: {1}".format(s, str(e)))
        return -1
    except TypeError as e:
        print("conversion failed due to TypeError, unable to convert '{0}' to an integer. The exception message is: {1}".format(s, str(e)))
        return -1


def divide(s, t):
    '''convert the two values: s and t to an integer, then calculate the result of s/t'''
    try:
        x = int(s)
        y = int(t)
        z = x/y
        print("conversion is successful")
        return z
    except ValueError as e:
        print("conversion failed due to ValueError. The exception message is: {0}".format(str(e)))
        return -1
    except TypeError as e:
        print("conversion failed due to TypeError. The exception message is: {0}".format(str(e)))
        return -1
    except Exception as e:
        print("conversion failed due to a general exception. The exception message is: {0}".format(str(e)))
        return -1

#i = convertToInt4("5")
#print(i)
#j = convertToInt4("dog")    
#print(j)
#k = convertToInt4([1, 2, 3])
#print(k)
l = divide(4, 0)
print(l)