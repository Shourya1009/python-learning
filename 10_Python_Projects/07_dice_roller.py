# advanced_dice_roller.py
import random

roll_history = []

def roll_dice(num_dice=1, sides=6):
    results = [random.randint(1, sides) for _ in range(num_dice)]
    roll_history.append(results)
    return results

def view_history():
    if not roll_history:
        print("📭 No rolls yet!")
    else:
        print("\n📜 Roll History:")
        for i, roll in enumerate(roll_history, start=1):
            print(f"Roll {i}: {roll}")

def main():
    print("🎲 Advanced Dice Roller 🎲")
    
    while True:
        print("\nOptions:")
        print("1. Roll Dice")
        print("2. View Roll History")
        print("3. Clear History")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            try:
                num_dice = int(input("How many dice do you want to roll? "))
                sides = int(input("How many sides should the dice have? (e.g., 6, 8, 12, 20): "))
                results = roll_dice(num_dice, sides)
                print(f"➡️ You rolled: {results} (Total: {sum(results)})")
            except ValueError:
                print("⚠️ Please enter valid numbers.")
        
        elif choice == "2":
            view_history()
        
        elif choice == "3":
            roll_history.clear()
            print("🧹 History cleared!")
        
        elif choice == "4":
            print("👋 Thanks for playing! Goodbye.")
            break
        
        else:
            print("⚠️ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
