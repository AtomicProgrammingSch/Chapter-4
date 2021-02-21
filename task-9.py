def power_value(number, exponent):
    return number ** exponent


print("Please enter your number:")
number = float(input())
print("Please enter your exponent:")
exponent = float(input())
# float is used to allow decimal numbers to be used
print("{} to the power of {} is {}".format(
    str(number), str(exponent), str(power_value(number, exponent))
))
