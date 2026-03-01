#DiceRoll.py
#Name: Rinku Mahato
#Date:02/28/2026
#Assignment: Dice roll

import random

def main():
    rolls = 10000 

    # list for totals 2..12 → 11 slots
    totals = [0] * 11

    # simulate rolls
    for r in range(rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum = dice1 + dice2
        totals[sum - 2] += 1  # index shift: total 2 → index 0

    # print header
    print(f"Total rolls: {rolls}\n")
    print("Total : Count : Percent")

    # print statistics for dice rolls
    for total in range(2, 13):
        count = totals[total - 2]
        percent = (count / rolls) * 100
        print(f"{total:>5} : {count:>5} : {percent:6.2f}%")

if __name__ == "__main__":
    main()