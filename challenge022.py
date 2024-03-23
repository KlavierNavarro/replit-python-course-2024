#Challenge 022 - Use other people's code
import random

print("Welcome to the Guess the Number Game!")
number = random.randint(1, 1000000)
guess = 0
attempts = 1

while guess != number:
  guess = int(input("Guess a number between 1 and 1000000: "))
  if guess < 0:
    print("Hey, that's cheating! Game over!")
    exit()
  elif guess < number:
    print("That's too low, try again!")
    attempts += 1
  elif guess > number:
    print("That's too high, try again!")
    attempts += 1
  else:
    print(f"You won! It took you {attempts} attempt(s)")
