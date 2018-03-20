"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A value error will occur if you use and invalid number like $,@,%, or +.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if you attempt to divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes
"""

try:
    denominator = 0
    numerator = int(input("Enter the numerator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("It cannot be divided by zero")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")