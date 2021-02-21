def tail_name(name):
    tail = len(name)
    tail_name = name[1:tail]
    print("The tail for the name {} is {}".format(name, tail_name))


print("Please enter your name:")
name = input()
tail_name(name)
