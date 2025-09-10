# password_generator.py
import random
import string

def generate_password(length=12):
    # Define characters (letters, digits, symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 4:
            print("⚠️ Password length should be at least 4.")
            return
        password = generate_password(length)
        print(f"✅ Your generated password: {password}")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
