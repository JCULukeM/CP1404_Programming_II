
def first_last_in_list(numbers_list):
    print("The first number is {}".format(numbers_list[0]))
    print("The last number is {}".format(numbers_list[-1]))


def smallest_largest_in_list(numbers_list):
    print("The smallest number is {}".format(min(numbers_list)))
    print("The biggest number is {}".format(max(numbers_list)))


def list_average(numbers_list):
    list_length = len(numbers_list)
    average = sum(numbers_list) / list_length
    print("The average of the list is {}".format(average))

def main():
    numbers_list = []
    number_counter = 5
    while number_counter > 0:
        number = int(input("Number: "))
        numbers_list.append(number)
        number_counter -= 1

    first_last_in_list(numbers_list)
    smallest_largest_in_list(numbers_list)
    list_average(numbers_list)
    print(numbers_list)




main()