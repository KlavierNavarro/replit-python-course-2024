#Challenge 009 - Generation Generator
print("Generation Generator")
year = int(input("What year were you born? "))
if year <= 1924:
  print("You are too old!")
elif year > 1924 and year <= 1946:
  print("You are a Traditionalist.")
elif year > 1946 and year <= 1964:
  print("You are a Baby Boomer.")
elif year > 1964 and year <= 1981:
  print("You are a Gen X.")
elif year > 1981 and year <= 1995:
  print("You are a Millenial.")
elif year > 1995 and year <= 2015:
  print("You are a Gen Z.")
else:
  print("You are a baby!")