def area_of_circle(r):
    return 22/7 * r ** 2


print("Please enter the radius of the circle:")
radius = float(input())  # used float to allow decimal input
print("The area of the circle is " + str(area_of_circle(radius)))
