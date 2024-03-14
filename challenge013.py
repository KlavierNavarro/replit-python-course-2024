#Challenge 013 - Grade Generator
test = input("What is the name of the test? ")
max = int(input("What is the maximum score? "))
score = float(input("How many points did you receive? "))

percent = round(score / max * 100, 2)
if percent >= 90:
  grade = "A+"
  article = "an"
  color = "\033[35m"
elif percent >= 80:
  grade = "A"
  article = "an"
  color = "\033[32m"
elif percent >= 70:
  grade = "B"
  article = "a"
  color = "\033[36m"
elif percent >= 60:
  grade = "C"
  article = "a"
  color = "\033[93m"
elif percent >= 50:
  grade = "D"
  article = "a"
  color = "\033[33m"
else:
  grade = "U"
  article = "a"
  color = "\033[31m"
  
print(f"You got {percent}%, which is {article} {color}{grade}")