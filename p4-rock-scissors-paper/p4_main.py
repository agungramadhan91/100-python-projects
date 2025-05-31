import random

options = ["🪨","📜","✂️"]

choose_type = input("Choose number: 1-Rock, 2-Paper, 3-Scissors: ")

user_choice = int(choose_type) - 1
comp_choice = random.randint(0,2)

print(type(user_choice))
print(f"User choice: {options[user_choice]}")
print(f"Computer choice: {options[comp_choice]}")

if user_choice == comp_choice:
    print("Draw!!!")
elif user_choice == 0 and comp_choice == 2:
    print("You Win!")
elif user_choice == 1 and comp_choice == 0:
    print("You Win!")
elif user_choice == 2 and comp_choice == 1:
    print("You Win!")
else:
    print("You Lose!")
