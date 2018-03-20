
def main():
    item_total = 0
    num_items = -1
    while num_items < 0:
        num_items = int(input("How many items"))
        if num_items < 0:
            print("Invalid number!")
    while num_items > 0:
        item_price = float(input("Price of item"))
        num_items -= 1
        item_total += item_price

    if item_total > 100:
        item_total -= item_total * 0.1
    print(item_total)

main()
