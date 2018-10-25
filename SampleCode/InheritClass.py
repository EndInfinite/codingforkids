class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("enter the sides:" + str(i+1) + ":")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("sides", i+1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("the area of  the triangle is %0.2f" %area)


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

