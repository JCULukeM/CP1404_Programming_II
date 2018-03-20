
OUTPUT_FILE = 'name.txt'

def program_1():

    out_file = open(OUTPUT_FILE, 'w')
    name = input("What is your name")
    print(name, file=out_file)
    out_file.close()
program_1()


def program_2():
    in_file = open(OUTPUT_FILE, 'r')
    name = in_file.read().strip()
    print("Your name is", name)
    in_file.close()
program_2()


def program_3():
    OUTPUT_FILE_2 = 'numbers.txt'
    in_file = open(OUTPUT_FILE_2, 'r')
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(first_number + second_number)
    in_file.close()
program_3()

