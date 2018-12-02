myList = list(range(1, 101))

sum1 = 0
sum2 = 0
for i in myList:
    sum1 = sum1 + pow(i, 2)
    sum2 = sum2 + i

sum2 = pow(sum2, 2)

diff = sum2 - sum1
print("the difference is:", diff)

#the difference is: 25164150

