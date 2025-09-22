import random

def main():
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "brown"]
    chosen_color = random.choice(colors)
    attempts = 0

    print("🎨 Welcome to the Color Guessing Game!")
    print("I have chosen a color from this list:")
    print(", ".join(colors))
    print("Try to guess it. Type 'quit' to exit.\n")

    while True:
        guess = input("Your guess: ").lower()
        if guess == "quit":
            print(f"The color was: {chosen_color}. Goodbye!")
            break

        attempts += 1

        if guess not in colors:
            print("That's not in the list. Try again.")
            continue

        if guess == chosen_color:
            print(f"🎉 Correct! The color was '{chosen_color}'. You guessed it in {attempts} attempts.")
            break
        else:
            # Provide a simple alphabetical hint
            if guess < chosen_color:
                print("Hint: The color is alphabetically after your guess.")
            else:
                print("Hint: The color is alphabetically before your guess.")

if __name__ == "__main__":
    main()
