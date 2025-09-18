
def calculate_bmi(weight, height):
    """Calculate BMI = weight(kg) / height(m)^2"""
    return weight / (height ** 2)

def main():
    print("⚖️  BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)

        print(f"Your BMI is: {bmi:.2f}")

        # Simple interpretation
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
