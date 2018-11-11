count1 = 0
count2 = 0
namelist = ["Clinton Preston","Lula Whiteley","Harry Potter","Tom Riddle","Luna Lovegood", "Timmy", "Johnny","Marie","Ivy","Hermione"]

for myfriendname in namelist:
    a = (len(myfriendname))

    if a >= 12:
        print("this name is long")
        count1 = count1 + 1
    if a < 12:
        print("this name is short")
        count2 = count2 + 1
    print(myfriendname)

print(count1)
print(count2)