friends = ["Hou Jiawei", "Chen Yixuan", "Lei Siqi", "Lim Ming Xuan", "Zhao Yuxuan", "Darren Wong",
 "Chua Zern Hee", "Ryan Neo", "Dave van der Heijden", "Keenan Low"]
count1 = 0
count2 = 0

for i in range(10):
    if len(friends[i]) >= 12:
        count1 = count1 + 1
    else:
        count2 = count2+ 1
    
print("Count 1 is", count1)
print("Count 2 is", count2) 

    