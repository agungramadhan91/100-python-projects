import random

# Hangman stages (for each wrong guess)
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

# Word list
WORDS = ['python', 'hangman', 'challenge', 'programming', 'openai', 'terminal']

def get_random_word():
    return random.choice(WORDS).lower()

def display_game_state(hidden_word, guessed_letters, attempts):
    print(HANGMAN_PICS[attempts])
    print("Word: ", " ".join(hidden_word))
    print("Guessed letters: ", ", ".join(sorted(guessed_letters)))
    print()

def play_hangman():
    word = get_random_word()
    hidden_word = ['_' for _ in word]
    guessed_letters = set()
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman!\n")

    while attempts < max_attempts and '_' in hidden_word:
        display_game_state(hidden_word, guessed_letters, attempts)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    hidden_word[idx] = guess
            print("✅ Correct!\n")
        else:
            attempts += 1
            print("❌ Wrong guess!\n")

    display_game_state(hidden_word, guessed_letters, attempts)
    if '_' not in hidden_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 You lost. The word was:", word)

# Run the game
if __name__ == "__main__":
    play_hangman()
