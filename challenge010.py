#Challenge 010 - Extend your bill calculator
totalBill = float(input("What is the total bill amount? "))
tip = float(input("What percentage tip would you like to leave? "))
totalBill = totalBill + (totalBill * (tip/100))
people = int(input("How many people are splitting the bill? "))
print(f"Each person should pay: {totalBill/people}")