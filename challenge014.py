#Challenge 014 - 2 player rock, paper, scissors
from getpass import getpass as input

print("Rock, paper, scissors battle!")
player_1 = input("Player 1, select your move (R, P, or S): ")
player_2 = input("Player 2, select your move (R, P, or S): ")

if player_1 == player_2:
  print("It's a tie!")
elif player_1.upper() == "R":
  if player_2.upper() == "S":
    print("Player 1's rock wins against player 2's scissors!")
  elif player_2.upper() == "P":
    print("Player 2's paper wins against player 1's rock!")
  else:
    print("Invalid move player 2!")
elif player_1.upper() == "P":
  if player_2.upper() == "R":
    print("Player 1's paper wins against player 2's rock!")
  elif player_2.upper() == "S":
    print("Player 2's scissors win against player 1's paper!")
  else:
    print("Invalid move player 2!")
elif player_1.upper() == "S":
  if player_2.upper() == "P":
    print("Player 1's scissors win against player 2's paper!")
  elif player_2.upper() == "R":
    print("Player 2's rock wins against player 1's scissors!")
  else:
    print("Invalid move player 2!")
else:
  print("Invalid move player 1!")
