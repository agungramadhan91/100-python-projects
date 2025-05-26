import random

names_string = input("Give me everybody's names, separated by comma: ")
names = names_string.split(", ")

# Way 1
# boss = random.randint(0, len(names) - 1)
# print(f"{names[boss]} is going to buy meal today!")

# Way 2
boss = random.choice(names)
print(f"{boss} is going to buy meal today!")