class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def isSolvable(self):
        return self.__a * self.__d - self.__b * self.__c != 0

    def getX(self):
        if self.isSolvable():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return None

    def getY(self):
        if self.isSolvable():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return None

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
e = float(input("Enter the value of e: "))
f = float(input("Enter the value of f: "))

equation = LinearEquation(a, b, c, d, e, f)
print("\nSolution:")
if equation.isSolvable():
    print("x =", equation.getX())
    print("y =", equation.getY())
else:
    print("The equation is not solvable.")



