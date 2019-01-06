'''open a file and write some text into it'''
import sys

def writeToFile():
    f = open("myfile.txt", mode="wt", encoding="utf-8")  #try encoding="utf-8", or encoding="ascii" which doesn't support unicode
    f.write("my name is greggy.")
    f.write("I am a 3 years old boy.\n")
    f.write("what is your name?\n")
    f.write("nice to see you.\n")
    f.write("我的老家在杭州。\n")
    f.close()



def writeToFile2():
    '''delete the content in the file if any, then write the below new content intot it'''
    f = open("myfile.txt", mode="wt", encoding="utf-8")  #try encoding="utf-8", or encoding="ascii"
    f.write("PSLE is finally over!\n")
    f.write("郭靖的降龙十八掌天下无敌。\n")
    f.close()



def writeToFile3():
    '''append the new content after the existing content in the file'''
    f = open("myfile.txt", mode="at", encoding="utf-8")  #try encoding="utf-8", or encoding="ascii"
    f.write("PSLE is finally over!\n")
    f.write("郭靖的降龙十八掌天下无敌。\n")
    f.close()


def writeToFile4():
    '''handle the write exception'''
    try:
        f = open("myfile.txt", mode="wt", encoding="utf-8")  #try encoding="utf-8", or encoding="ascii"
        myList = ["I love Python!\n", "新加坡最好玩的地方是圣淘沙\n", "Minecraft is coded by Mojang\n"]
        for line in myList:
            try:
                f.write(line)
            except Exception as ex:
                print("Exception happened when reading the file. The error message is: {0}".format(str(ex)))
                continue
    finally:
        f.close()


def readFromFile():
    '''read the first line from the file'''
    f = open("myfile.txt", mode="rt", encoding="utf-8")
    s = f.readline()
    print(s)
    f.close()

def readFromFile2():
    '''read all the lines from the file'''
    f = open("myfile.txt", mode="rt", encoding="utf-8") 
    lines = f.readlines()
    print(lines)
    f.close()

def readFromFile3():
    '''iterate lines in for loop'''
    f = open("myfile.txt", mode="rt", encoding="utf-8")
    for line in f:
        #print(line)
        sys.stdout.write(line)
    f.close()

def readFromFile4():
    '''handle the read exception'''
    try:
        f = open("myfile.txt", mode="rt", encoding="ascii")     #try encoding="utf-8", or encoding="ascii"
        for line in f:
            #print(line)
            sys.stdout.write(line)
    except Exception as ex:
        print("Exception happened when reading the file. The error message is: {0}".format(str(ex)))
    finally:
        f.close()   #ensure the file will be defintely closed either there is no error or some exception happened


def modifyImageFile():
    '''open a binary file (a image file) and modify it, then save your changes to a new image file'''
    try:
        f1 = open("flower.jpg", mode="rb")     #binary mode doens't take any encoding
        fileData = f1.read()
        byteData = bytearray(fileData)
        for i in range(15000, 15100):
            byteData[i] = 0xfe
        f2 = open("modifiedflower.jpg", mode="wb")
        f2.write(byteData)
    except Exception as ex:
        print("Exception happened when reading the file. The error message is: {0}".format(str(ex)))
    finally:
        f1.close()   #ensure the file will be defintely closed either there is no error or some exception happened
        f2.close()

#writeToFile()
#writeToFile2()
#writeToFile3()
#writeToFile4()

#readFromFile()
#readFromFile2()
#readFromFile3()
#readFromFile4()
modifyImageFile()
