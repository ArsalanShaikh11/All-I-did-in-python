import random as R

def choose_word():
    # List of words for the Hangman game
    word_list = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple"]

    # Choose a random word from the list
    return R.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed, others hidden as underscores
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed = []
    Chance = 6  # Number of attempts allowed

    while Chance > 0:
        print("\n" + display_word(secret_word, guessed))
        if '_' not in display_word(secret_word, guessed):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)

        if guess not in secret_word:
            Chance -= 1
            print(f"Wrong guess! Attempts left: {Chance}")
            if Chance == 0:
                print("Sorry, you're out of attempts. The word was:", secret_word)
                break
        else:
            print("Good guess!")

if __name__ == "__main__":
    hangman()
