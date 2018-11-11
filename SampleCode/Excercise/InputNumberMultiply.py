def multiply2Number(number1, number2):
    result = number1 * number2
    return result


a = int(input("please key in the first number:"))
b = int(input("please key in the second number:"))

c = multiply2Number(a, b)
print("The multiply result of {0} and {1} is: {2}".format(a, b, c))
