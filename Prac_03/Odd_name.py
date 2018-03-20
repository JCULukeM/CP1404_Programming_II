"""Luke Maclean"""


def method_name(name,num_letters):
    print("".join(name[::num_letters]))


def get_name():
    name = ""
    while name == "":
        name = input("What is your name")
        if name == "":
            print("Invalid name")
    return name


def main():
    name = get_name()
    num_letters = int(input("Where would you like to split?"))
    method_name(name, num_letters)


main()
