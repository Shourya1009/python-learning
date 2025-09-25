import random

def roll_dice(sides=6, rolls=1):
    """Roll a dice with given number of sides and rolls."""
    return [random.randint(1, sides) for _ in range(rolls)]

def main():
    print("🎲 Dice Roller 🎲")
    while True:
        try:
            sides = int(input("Enter number of sides on the dice (e.g. 6): "))
            rolls = int(input("Enter how many dice to roll: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        results = roll_dice(sides, rolls)
        print(f"You rolled: {results} (Total: {sum(results)})")

        again = input("Roll again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
