#Challenge 007 - Fake Fan Question Generator
print("Fake Fan Question Generator")
videogame = input("What is your favorite videogame? ")
if videogame.lower() in ["pokemon", "pokémon"]:
  favePokemon = input("Oh, really? What's your favorite Pokémon? ")
  if favePokemon.lower() in ["ninetales", "salamence", "hawlucha", "tatsugiri", "rowlet"]:
    print("Right answer")
  elif favePokemon in ["pikachu", "charmander", "charizard"]:
    print("Nah, Ninetales is better")
  else:
    print("That's okay... I guess")
elif videogame.lower() in ["minecraft", "roblox", "fortnite"]:
  print("Ew, that's a bad game.")
else:
  print("Yeah, that's cool and all...")