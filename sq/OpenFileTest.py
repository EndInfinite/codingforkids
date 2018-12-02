import sys

def writeToFile():
    f = open("myfile.txt", mode="wt", encoding="ascii") #"utf-8"
    f.write("my name is Nobody.")
    f.write("I am 12.\n")
    f.write("Who are you?\n")
    f.write("Why are you here?\n")
    f.write("o(*￣▽￣*)ブ\n")
    f.close()

writeToFile()