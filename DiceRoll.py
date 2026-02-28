#DiceRoll.py
#Name: Rinku Mahato
#Date:02/28/2026
#Assignment: Dice roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0] * 13
  trials = 10000
  #Create two dice values ranging from 1 - 6 each
  for r in range(trials):
    dice1 = random.randint(1,6)
    dice2 = random.randint (1,6)
   #find the sum total of the two dice
    total = dice1 + dice2
    rolls [total] += 1
  #print statictics for dice rolls
    print("sum\tcount\tpercentage")
    print("-" * 30)

    total_rolls = sum(rolls)
    total_percentage = 0.0

    for total in range (2, 13):
      count = rolls[total]
      percentage = (count / total_rolls) * 100 
      total_percentage += percentage
      print(f"{total}\t{count}\t{percentage:.2f}%")

    print("-" * 30)
    print("total rolls counted:", total_rolls)
    print(f"sum of percentages: {total_percentage:.2f}% ((should be ~100%)")


  if __name__ == '__main__':
   main()

  