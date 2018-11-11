class Dog:
    

    def __init__(self, name):
        self.name = name
        self.tricks = []
        self.color = ""
    
    def __str__(self):
        return "Dog " + self.name

    def addTrick(self, trick):
        self.tricks.append(trick)

    def setColor(self, color):
        self.color = color

dog1 = Dog("Greg")
dog2 = Dog("Fido")

dog1.addTrick("roll over")
dog1.addTrick("shake hand")

dog2.addTrick("play dead")
dog2.addTrick("show belly")

dog1.setColor("yellow")
dog2.setColor("brown")

print(dog1.name)
print(dog1.color)
print(list(dog1.tricks))
print(dog1)

print("\n")

print(dog2.name)
print(dog2.color)
print(list(dog2.tricks))
