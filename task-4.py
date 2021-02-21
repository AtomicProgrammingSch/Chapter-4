def hello_three_times(name):
    for i in range(3):
        print("Hello {}".format(name))


print("Please enter your name:")
name = input()
hello_three_times(name)
