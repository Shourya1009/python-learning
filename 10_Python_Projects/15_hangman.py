import random

# A small list of words for the game
words = ["python", "hangman", "developer", "program", "keyboard", "function", "variable"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main():
    print("🎮 Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # number of allowed wrong guesses

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"❌ {guess} is not in the word.")
        else:
            print(f"✅ Good job! {guess} is in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You won! The word was '{word}'.")
            break
    else:
        print(f"\n💀 You lost! The word was '{word}'.")

if __name__ == "__main__":
    main()
