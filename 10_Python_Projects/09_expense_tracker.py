# expense_tracker.py

expenses = []

def show_menu():
    print("\n💰 Expense Tracker")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Exit")

def add_expense():
    try:
        description = input("Enter description: ")
        amount = float(input("Enter amount: ₹"))
        expenses.append({"description": description, "amount": amount})
        print(f"✅ Added: {description} - ₹{amount}")
    except ValueError:
        print("⚠️ Invalid amount entered.")

def view_expenses():
    if not expenses:
        print("📭 No expenses yet!")
    else:
        print("\nYour Expenses:")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['description']} - ₹{exp['amount']}")

def view_total():
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n💵 Total Spent: ₹{total}")

def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    main()
