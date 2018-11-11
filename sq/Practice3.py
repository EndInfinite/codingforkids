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

"""#Define a list containing 10 names of your friends, check and record the count of your friends 
whose name has 12 or more characters, as well as your friends whose name has less than 12 characters,
then print out the two respective counts."""
