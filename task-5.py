def head_name(name):
    char = name[0]
    print("The first character in the name {} is {}".format(name, char))


print("Please enter your name:")
name = input()
head_name(name)
