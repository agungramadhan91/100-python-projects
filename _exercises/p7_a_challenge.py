import random

word_list = ["advark","baboon","camel"]
choosen_word = random.choice(word_list)
display = []

for _ in choosen_word:
    display += "_"

print(f"Hint: {len(choosen_word)} letters")

guess_word = input(f"\nGuess a letter: ").lower()

for position in range(len(choosen_word)):
    letter = choosen_word[position]

    if letter == guess_word:
        display[position] = letter
    else:
        display[position] = "_"

    # print(position)

for blank in display:
    print(blank) 

print(f"Answer: {display}")
