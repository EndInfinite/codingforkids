class Dog:
    onwer = "zujiang"
    def __init__(self, name):
        self.name = name
        self.__privateName = ""     #starting with __ to define a private variable in class
        self.tricks = ["bark"]
        self.color = ""
    
    def __str__(self):
        return "Dog " + self.name

    def addTrick(self, trick):
        self.tricks.append(trick)

    def setColor(self, color):
        self.color = color

    def setPrivateName(self, privateName):
        self.__privateName = privateName

    def getPrivateName(self):
        return self.__privateName

dog1 = Dog("Furry")
dog2 = Dog("Fido")

dog1.setColor("yellow")
dog1.addTrick("roll over")
dog1.addTrick("shake hand")

dog2.setColor("brown")
dog2.addTrick("show belly")

print("dog1 name is:", dog1.name)
print("dog1 color is:", dog1.color)
print("dog1 can play tricks:", list(dog1.tricks))
print("dog1's owner is:", dog1.onwer)

print("\n")

print("dog2 name is:", dog2.name)
print("dog2 color is:", dog2.color)
print("dog2 can play tricks:", list(dog2.tricks))
print("dog2's owner is:", dog2.onwer)

print("\n")

#test the private name in class
dog1.setPrivateName("gougou")
try:
    print(dog1.__privateName)
except:
    print("__privateName is not accessible from outside of the class.")
print("we can get the privateName of dog1 by calling getPrivateName() method:", dog1.getPrivateName())