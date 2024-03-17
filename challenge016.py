#Challenge 016 - Name the Lyrics
print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)""")

counter = 1
while True:
  print("Never gonna ____ you up.")
  word = input()
  if word.lower() == "give":
    break
  else:
    print("Nope, try again.")
    counter += 1
print(f"Well done! It only took you {counter} attempt(s).")
