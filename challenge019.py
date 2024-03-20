#Challenge 019 - Loan Calculator
loan = 1000
apr = 0.05
for i in range(10):
  loan += (loan * apr)
  print(f"Year {i + 1} is {round(loan, 2)}")
