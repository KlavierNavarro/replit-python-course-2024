#Challenge 017 - Let's (Cheat) Continue
from getpass import getpass as input

print("Rock, paper, scissors battle!")
score_1 = 0
score_2 = 0
while True:
  player_1 = input("Player 1, select your move (R, P, or S): ")
  player_2 = input("Player 2, select your move (R, P, or S): ")
  
  if player_1 == player_2:
    print("It's a tie!")
  elif player_1.upper() == "R":
    if player_2.upper() == "S":
      print("Player 1's rock wins against player 2's scissors!")
      score_1 += 1
    elif player_2.upper() == "P":
      print("Player 2's paper wins against player 1's rock!")
      score_2 += 1
    else:
      print("Invalid move player 2!")
  elif player_1.upper() == "P":
    if player_2.upper() == "R":
      print("Player 1's paper wins against player 2's rock!")
      score_1 += 1
    elif player_2.upper() == "S":
      print("Player 2's scissors win against player 1's paper!")
      score_2 += 1
    else:
      print("Invalid move player 2!")
  elif player_1.upper() == "S":
    if player_2.upper() == "P":
      print("Player 1's scissors win against player 2's paper!")
      score_1 += 1
    elif player_2.upper() == "R":
      print("Player 2's rock wins against player 1's scissors!")
      score_2 += 1
    else:
      print("Invalid move player 2!")
  else:
    print("Invalid move player 1!")
  print(f"Player 1's score: {score_1}")
  print(f"Player 2's score: {score_2}")

  if score_1 == 3 or score_2 == 3:
    print("Thanks for playing!")
    exit()
  else:
    continue
