#Challenge 027 - Video Game Characters
import os, time, random, math
def createCharacter():
    name = input("Name your character: ")
    race = input("Select your character's race (human, imp, demon, orc, elf...): ")
    print(f"{name} the {race}")

def rollDice(sides):
    return random.randint(1, sides)

def generateStats():
    return math.trunc(rollDice(6) * rollDice(12) / 2 + 10)

again = True
while again:
    os.system("clear")
    print("Character Builder")
    time.sleep(1)
    createCharacter()
    time.sleep(1)
    print(f"HEALTH: {generateStats()}")
    time.sleep(1)
    print(f"ATTACK: {generateStats()}")
    time.sleep(1)
    print(f"DEFENSE: {generateStats()}")
    time.sleep(1)
    print(f"SPEED: {generateStats()}")
    time.sleep(1)
    repeat = input("Do you want to generate another character? (yes/no): ")
    if repeat != "yes":
        again = False