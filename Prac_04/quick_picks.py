from random import randint

MINIMUM = 1
MAXIMUM = 45


def quick_pick_line():
    lotto_line = []
    num = 6
    while num > 0:
        lotto_num = randint(MINIMUM, MAXIMUM)
        if lotto_num not in lotto_line:
            num -= 1
            lotto_line.append(lotto_num)

    lotto_line.sort()
    return lotto_line


def main():
    num_quick_picks = int(input("How many quick picks"))

    while num_quick_picks > 0:
        num_quick_picks -= 1
        lotto_line = quick_pick_line()
        print("")
        for i in lotto_line:
            print("{:2}".format(i), end=' ')

main()
