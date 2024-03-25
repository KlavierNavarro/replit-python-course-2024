#Challenge 024 - Infinity Dice
import random

def rollDice(sides):
    print(f"You rolled {random.randint(1, sides)}")
    play = input("Roll again? (yes/no): ")
    return True if play == "yes" else False

print("Infinity Dice!")

play = True

while play:
    sides = int(input("How many sides? "))
    play = rollDice(sides)