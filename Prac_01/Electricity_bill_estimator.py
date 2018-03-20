TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():

    tariff = int(input("Which tariff? 11 or 31 "))
    if tariff == 11:
        tariff = TARIFF_11
    else:
        tariff = TARIFF_31
    daily_use = float(input("Enter daily kWh usage"))
    num_bill_days = float(input("Enter number of billing days"))
    daily_cost = (daily_use * tariff)
    bill = daily_cost * num_bill_days
    print("Estimated bill: ", bill)
main()