#Challenge 025 - Health Stats Generator
import random

def rollDice(sides):
    return random.randint(1, sides)

def generateHealth(name):
    print(f"{name}'s health is {rollDice(6)*rollDice(8)}hp")
    again = input("Do you want to generate health for another character? (yes/no): ")
    return True if again == "yes" else False

print("Character Health Generator")

again = True

while again:
    name = input("Name your warrior: ")
    again = generateHealth(name)