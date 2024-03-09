#Challenge 008 - Affirmations (or insults) Generator
name = input("What's your name? ")
weekDay = input("What day of the week is it? ")

if weekDay.lower() == "monday":
  food = input("Tell me your favorite food: ")
  print(f"Hey {name}, you're going to have a great Monday! You're going to eat {food}")
elif weekDay.lower() == "tuesday":
  singer = input("Who's your favorite singer? ")
  print(f"Hey {name}, you're going to have a great Tuesday! You're going to listen to {singer}")
elif weekDay.lower() == "wednesday":
  videogame = input("What's your favorite video game? ")
  print(f"Hey {name}, you're going to have a great Wednesday! You're going to play {videogame}")
elif weekDay.lower() == "thursday":
  language = input("What's your favorite programming language? ")
  print(f"Hey {name}, you're going to have a great Thursday! You're going to code in {language}")
elif weekDay.lower() == "friday":
  movie = input("What's your favorite movie? ")
  print(f"Hey {name}, you're going to have a great Friday! You're going to watch {movie}")
else:
  print("I don't know that day of the week, but I hope you have fun!")