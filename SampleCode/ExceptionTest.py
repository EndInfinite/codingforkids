class Error(Exception):
    """Base class for other Exception"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input vlaue is too large"""

number = 10

while True:
    try:
        i_num = int(input("enter a number:"))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("your value is too smal!")
        print()
    except ValueTooLargeError:
        print("your value is too large!")
        print()

print("your guess is correct!")

