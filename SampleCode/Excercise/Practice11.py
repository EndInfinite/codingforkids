#s = "7316717653133062491922511967442657474235534912493496353520312774506326239578318016944801869478851843"

s = "7316717653133062491922511967442657474235534912493496353520312774506326239578318016944807958478851843"

my4DigitList = []
largestProduct = 0
for i in range(len(s)-3):
    product = int(s[i])*int(s[i+1])*int(s[i+2])*int(s[i+3])
    if product > largestProduct:
        largestProduct = product
 
for i in range(len(s)-3):
    product = int(s[i])*int(s[i+1])*int(s[i+2])*int(s[i+3])
    if product == largestProduct:
        new4Digit = s[i] + s[i+1] + s[i+2] + s[i+3]
        my4DigitList.append(new4Digit)
    
print("the larget product from the 4 adjacent digit is:", largestProduct)
print("the four digits are:", my4DigitList)








