# quiz_game.py

def run_quiz():
    questions = {
        "1. What is the capital of France?": "paris",
        "2. Which planet is known as the Red Planet?": "mars",
        "3. Who developed Python programming language?": "guido van rossum",
        "4. What is 5 * 6?": "30",
        "5. Which data type is immutable in Python?": "tuple",
    }

    score = 0

    print("📝 Welcome to the Quiz Game!")
    print("Answer the following questions:\n")

    for question, answer in questions.items():
        user_answer = input(question + " ").lower()
        if user_answer == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}\n")

    print(f"🎉 Quiz Over! You scored {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
