import sys

def writeToFile():
    f = open("myfile.txt", mode="wt", encoding="utf-8") #don't use ascii
    f.write("my name is Nobody.")
    f.write("I am 12.\n")
    f.write("Who are you?\n")
    f.write("Why are you here?\n")
    f.write("o(*￣▽￣*)ブ\n")
    f.close()

def writeToFile2():
    f = open("myfile.txt", mode="wt", encoding="utf-8")
    f.write("My PSLE result is XXX\n")
    f.write("我很伤心。\n")
    f.close()

def writeToFile3():
    f = open("myfile.txt", mode="at", encoding="utf-8")
    f.write("My PSLE result is XXX\n")
    f.write("我很伤心。\n")
    f.close()

writeToFile()
writeToFile3()