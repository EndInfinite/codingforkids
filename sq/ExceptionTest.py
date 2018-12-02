def convertToInt(s):
    x = int(s)
    print("conversion is successful, the converted value is:", x)
    return x

def convertToInt2(s):
    try:
        x = int(s)
        print("conversion is successful, the converted value is:", x)
        return x
    except ValueError
        print("conversion failed, unable to convert '{0}' to an integer.".format(s))
        return -1

