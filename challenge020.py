#Challenge 020 - List Generator
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
increment = int(input("Enter an increment: "))

for i in range(start, end, increment):
  print(i)
