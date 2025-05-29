import random

word_list       = ["advark","baboon","camel"]
choosen_word    = random.choice(word_list)
display         = []

for _ in choosen_word:
    display += "_"

print(display)

guess_word      = input("Guess a letter: ").lower()

for position in range(len(choosen_word)):
    letter = choosen_word[position]

    if letter == guess_word:
        display[position] = letter
    else:
        display[position] = "_"

print(display)