from math import pi  # using the variable defined in the math module as pi


def area_of_circle(r):
    return pi * r ** 2


print("Please enter the radius of the circle:")
radius = float(input())
print("The area of the circle is: " + str(area_of_circle(radius)))
