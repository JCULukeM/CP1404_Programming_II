
def menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

def main():
    name = input("What is your name")
    (menu())
    choice = input("Choose an option").upper()
    while choice != 'Q':
        if choice == 'H':
            print("Hello ", name)
        elif choice == 'G':
            print("Goodbye", name)
        else:
            print("Invalid choice")
        (menu())
        choice = input("Choose an option").upper()
        
    print("Finished")
main()