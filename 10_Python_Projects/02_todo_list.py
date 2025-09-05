# todo_list_app.py

tasks = []

def show_menu():
    print("\n📋 TO-DO LIST APP")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added!")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"❌ Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("⚠️ Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Exiting To-Do List App. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again!")

if __name__ == "__main__":
    main()
