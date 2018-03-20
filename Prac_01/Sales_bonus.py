"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = 1
    while sales >0:
        bonus = 0
        sales = float(input("Enter sales: $"))
        if sales < 1000:
            bonus = 0.1
        elif sales >= 1000:
            bonus = 0.15

        result = sales * bonus
        print("You get a bonus of $", result)
main()
