#Challenge 028 - Epic Character Battle
import os, time, random, math

class Character:
    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
    
    def takeDamage(self, damage):
        self.health -= damage

def rollDice(sides):
    return random.randint(1, sides)

def generateStats():
    return math.trunc(rollDice(6) * rollDice(12) / 2 + 10)

def createCharacter():
    name = input("Name your character: ")
    race = input("Select your character's race (human, imp, demon, orc, elf...): ")
    health = generateStats()
    attack = generateStats()
    return Character(name, race, health, attack)

def printCharacter(character):
    print(f"{character.name} the {character.race}")
    time.sleep(1)
    print(f"HEALTH: {character.health}")
    time.sleep(1)
    print(f"ATTACK: {character.attack}")
    time.sleep(1)

def battle(character1, character2):
    print("BATTLE TIME")
    print()
    if character1.attack > character2.attack:
        attackDifference = character1.attack - character2.attack
    elif character1.attack < character2.attack:
        attackDifference = character2.attack - character1.attack
    else:
        attackDifference = 1

    counter = 0
    while character1.health > 0 and character2.health > 0:
        dice1 = rollDice(6)
        dice2 = rollDice(6)
        if dice1 > dice2:
            print(f"{character1.name} wins the first blow")
            print(f"{character2.name} takes a hit, with {attackDifference} damage")
            character2.takeDamage(attackDifference)
            print
        elif dice1 < dice2:
            print(f"{character2.name} wins the first blow")
            print(f"{character1.name} takes a hit, with {attackDifference} damage")
            character1.takeDamage(attackDifference)
        else:
            print("It's a tie!")

        time.sleep(2)
        print()
        print(character1.name)
        print(f"HEALTH: {character1.health}")
        time.sleep(1)
        print()
        print(character2.name)
        print(f"HEALTH: {character2.health}")
        print()
        counter += 1

        if character1.health > 0 and character2.health > 0:
            print("And they're both standing for the next round!")
            time.sleep(1)
            print()
        elif character1.health <= 0:
            print(f"Oh no! {character1.name} has died!")
            print()
            print(f"{character2.name} destroyed {character1.name} in {counter} rounds!")
        elif character2.health <= 0:
            print(f"Oh no! {character2.name} has died!")
            print()
            print(f"{character1.name} destroyed {character2.name} in {counter} rounds!")

os.system("clear")
print("Character Builder")
time.sleep(1)
character1 = createCharacter()
printCharacter(character1)
print()
print("Who are the battling?")
print()
time.sleep(1)
character2 = createCharacter()
printCharacter(character2)
os.system("clear")
battle(character1, character2)