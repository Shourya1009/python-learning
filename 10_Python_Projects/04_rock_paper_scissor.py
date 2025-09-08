# rock_paper_scissors.py
import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock, Paper, Scissors!")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user_choice == "exit":
            print("👋 Thanks for playing! Goodbye!")
            break

        if user_choice not in choices:
            print("⚠️ Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("🎉 You win!")
        else:
            print("💀 You lose!")

if __name__ == "__main__":
    rock_paper_scissors()
