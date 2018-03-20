def menu():
    print("(E)Show the even numbers from x to y")
    print("(O)Show the odd numbers from x to y")
    print("(S)Show the squares from x to y")
    print("(Q)uit")


def main():
    (menu())
    choice = input("Choose an option").upper()
    while choice != 'Q':
        if choice == 'E':
            x_choice = int(input("Choose an (x)First number"))
            if x_choice % 2 == 1:
                x_choice += 1
            y_choice = int(input("Choose (y)Last number"))
            for i in range(x_choice, y_choice, 2):
                print(i, end=' ')
            print()

        elif choice == 'O':
            x_choice = int(input("Choose an (x)First number"))
            if x_choice % 2 == 0:
                x_choice += 1
            y_choice = int(input("Choose (y)Last number"))
            for i in range(x_choice, y_choice, 2):
                print(i, end=' ')
            print()

        elif choice == 'S':
            x_choice = int(input("Choose an (x)First number"))
            y_choice = int(input("Choose (y)Last number"))
            for i in range(x_choice, y_choice, 1):
                print(i ** (1/2), end=' ')
            print()
        else:
            print("Invalid choice")
        (menu())
        choice = input("Choose an option").upper()

    print("Finished")


main()