#Challenge 011 - How many seconds are in a year?
year = int(input("What year is it? "))
leapYear = year % 4 == 0

if leapYear:
  print(f"There are {366 * 24 * 60 * 60} seconds in {year}, as it is a leap year.")
else:
  print(f"There are {365 * 24 * 60 * 60} seconds in {year}")