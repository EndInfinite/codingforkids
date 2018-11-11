from math import factorial

a = factorial(5)
b = factorial(5-3)
c = factorial(3)

result = int(a / (b * c))
print("there are {} ways to take 3 fruits from 5 fruits".format(result))

