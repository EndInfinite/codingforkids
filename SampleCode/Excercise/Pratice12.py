import math

for a in range(1000):
    for b in range(1000):
        result = a**2 + b**2
        c = math.sqrt(result)
        if a + b + c == 1000:
            print("a is {0}, b is {1}, c is {2}".format(a, b, c))

print("no solution found")

if math.sqrt(25) == 5:
    print("yes")

#result is: a = 200, b = 375, c = 425