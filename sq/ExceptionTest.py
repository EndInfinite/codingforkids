def convertToInt(s):
    x = int(s)
    print("conversion is successful, the converted value is:", x)
    return x

def convertToInt2(s):
    try:
        x = int(s)
        print("conversion is successful, the converted value is:", x)
        return x
    except ValueError:
        print("conversion failed, unable to convert '{0}' to an integer.".format(s))
        return -1

def convertToInt3(s):
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

def convertToInt5(s):
    try:
        x = int(s)
        print("conversion is successful, the converted value is:", x)
        return x
    except Exception as e:
        print("conversion failed due to ValueError, unable to convert '{0}' to an integer. The exception message is: {1}".format(s, str(e)))
        return -1
   

