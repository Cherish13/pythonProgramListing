import math
#this line imports the 'math' module, which provides mathematical functions like square root('sqrt')
class Quad:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        #this is the constructor method of the 'Quad', it initializes the object with coefficients 'a', 'b', and 'c'
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c
         #This are the getter methods that return the values of the coefficients 'a', 'b', 'c' respectively
    def setA(self, a):
        self.__a = a

    def setB(self, b):
        self.__b = b

    def setC(self, c):
        self.__c = c
          # this are the setters
    def getDiscr(self):
        return self.__b * self.__b - 4 * self.__a * self.__c

    def getRoot1(self):
        return (self.__b + math.sqrt(self.getDiscr()) / (2 * self.__a))

    def getRoot2(self):
        return (self.__b - math.sqrt(self.getDiscr()) / (2 * self.__a))

    def getPrint(self):
        if self.getDiscr() > 0:
            print("\nr1 =", self.getRoot1())
            print("r2 =", self.getRoot2())
        elif self.getDiscr() == 0:
            print("\nRepeated root: r =", self.getRoot1())
        else:
            print("\nThe equation has no real roots")

a, b, c = eval(input("Enter a, b, c: "))
quad = Quad(a, b, c)
quad.getPrint()
