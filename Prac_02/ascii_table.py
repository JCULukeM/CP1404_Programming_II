
LOWER = 33
UPPER = 127
def ascii_convert(character):
    ascii_num = ord(character)
    return ascii_num


def ascii_convert_value(character):
    ascii_num = chr(character)
    return ascii_num


def main():
    character = input("Enter a character: ")
    number = ascii_convert(character)
    print("The ASCII code for ", character, "is", number, )
    character_value = 55
    while character_value > LOWER and < UPPER:
        character_value = int(input("Enter a number between 33 and 127: "))
    number = ascii_convert_value(character_value)
    print("The ASCII code for ", character, "is", number, )
main()
