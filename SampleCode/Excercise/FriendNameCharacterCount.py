count1 = 0
count2 = 0

friends = ["Liu Xiuping", "Zhao Yuxuan", "Zhao Yixuan", "Lei Shiqi", "Tan Ah Meng", 
            "Wong Goo Lai", "Michael Jacson", "Donal Trump", "Lee Kuan Yoke", "Allan Walker"]

for name in friends:
    if(len(name) >= 12):
        count1 = count1 + 1
    else:
        count2 = count2 + 1

print("my friend counts whose name has 10 or more characters are: {0}".format(count1))
print("my friend counts whose name has less than 10 characters are: {0}".format(count2))
    
