import math

def circle_area(radius):
    return math.pi * radius**2

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print("The area of the circle is:", area)
