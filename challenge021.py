#Challenge 021 - Throwback to Math Facts
print("Math Game!")
table = int(input("Enter a number: "))
count = 0
for i in range(1, 11):
    result = int(input(f"{i} x {table} = "))
    if result == i * table:
        print("Great work!")
        count += 1
    else:
        print("No, the answer was", i * table)

print(f"You scored {count} out of 10")
