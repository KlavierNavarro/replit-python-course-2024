#Challenge 005 - "Which character are you?" Generator
print("""Ace Attorney Character Creator
I'm going to ask you some yes or no questions to determine which Ace Attorney character you are. Let's start!""")
smart = input("Are you smart? ")
if smart.lower() == "no":
  print("Aha! You're detective Gumshoe!")
else:
  print("Then you're not detective Gumshoe")
  memory = input("Have you ever lost your memory? ")
  if memory.lower() == "yes":
    print("Aha! You're Phoenix Wright!")
  else:
    print("Then you're not Phoenix Wright")
    hair = input("Do you have blue hair? ")
    if hair.lower() == "yes":
      print("Aha! You're Franziska von Karma!")
    else:
      print("Then you're not Franziska von Karma")
      sister = input("Do you know your sister's identity? ")
      if sister.lower() == "no":
        print("Aha! You're Apollo Justice!")
      else:
        print("Then you're not Apollo Justice")
        elevator = input("Have you ever gotten stuck on an elevator? ")
        if elevator.lower() == "yes":
          print("Aha! Then you're Miles Edgeworth!")
        else:
          print("Then you're not Miles Edgeworth")
          print("Who on earth are you?")