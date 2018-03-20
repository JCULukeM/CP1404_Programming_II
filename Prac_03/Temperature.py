"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def convert_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius()
            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":
            celsius = convert_fahrenheit()
            print("Result: {} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
main()