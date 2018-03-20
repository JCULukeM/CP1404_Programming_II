from random import randint

MINIMUM = 1
MAXIMUM = 45


def quick_pick_line():
    lotto_line = []
    num = 6
    while num > 0:
        num -= 1
        lotto_line.append(randint(MINIMUM, MAXIMUM))

    lotto_line.sort()
    print(lotto_line)


def main():
    num_quick_picks = int(input("How many quick picks"))

    while num_quick_picks > 0:
        num_quick_picks -= 1
        quick_pick_line()

main()
