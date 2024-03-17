#Challenge 015 - All About the Loop
exit = ""
while exit != "yes":
  animal = input("What animal do you want to hear? ")
  if animal.lower() == "cow":
    print("A cow goes moo.")
  elif animal.lower() == "dog":
    print("A dog goes woof.")
  elif animal.lower() == "cat":
    print("A cat goes meow.")
  elif animal.lower() == "sheep":
    print("A sheep goes baa.")
  elif animal.lower() == "pig":
    print("A pig goes oink.")
  elif animal.lower() == "chicken":
    print("A chicken goes cluck.")
  elif animal.lower() == "duck":
    print("A duck goes quack.")
  else:
    print("I don't know that animal.")

  exit = input("Do you want to exit? (yes/no): ")
