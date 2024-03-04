#Challenge 003 - The Ultimate Wacky Recipe Maker
print("""The Ultimate Wacky Recipe Maker
You'll be asked a bunch of questions and then we'll make you up an amazing recipe for today's evening meal.""")
food = input("Name a food: ")
plant = input("Name a plant: ")
method = input("Name a cooking method: ")
burned = input("How would you describe burned food?: ")
item = input("Name a household item: ")
hardware = input("Name a hardware piece: ")
element = input("Name an element of the periodic table: ")

print(method, food, "with", burned, plant, "on a bed of", item, "and a side of", hardware, "with", element, "dressing")