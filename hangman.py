import random

word_list = ["python", "hangman","programming","game","challenge","cat", "believe"]


def choose_word():
    return random.choice(word_list)

def display_word(word,guessed_letters):
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        return display

def hangman():
    selected_word = choose_word()
    guessed_letters = []
    attempts = 6 

    print("Welcome to hangman!")
    print(display_word(selected_word, guessed_letters))

    while True:
        guess= input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        print("Attempts left:", attempts)
        print(display_word(selected_word,guessed_letters))

        if "_" not in display_word(selected_word, guessed_letters):
            print("Congratulations! You've guessed the word:", selected_word)
            break

        if attempts == 0:
            print("Game over! The word was:", selected_word)
            break

if __name__ == "__main__":
            hangman()