class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.img = i 

    def getData(self):
        print("{0} + {1}j".format(self.real, self.img))


c1 = ComplexNumber(2, 3)
del c1.real

c1.getData()

