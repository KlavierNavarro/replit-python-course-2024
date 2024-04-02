#Challenge 030 - f...what?
print("30 Days Down")

for i in range(1, 31):
    opinion = input(f"What did you think of Day {i}? ")
    response = f'You thought day {i} was {opinion}'
    print(f'{response:^30}')