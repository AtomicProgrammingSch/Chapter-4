def perimeter_of_rectangle(l, w):
    return (l * 2) + (w * 2)


print("Please enter the length of the rectangle:")
length = float(input())
print("Please enter the width of the rectangle:")
width = float(input())

print("The perimeter of the rectangle is: " + str(perimeter_of_rectangle(length, width)))
