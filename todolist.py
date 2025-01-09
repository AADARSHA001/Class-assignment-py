# 7. Basic To-Do List
# Objective: Build a program to manage tasks.
# Steps:
# 1. Use a list to store tasks.
# 2. Provide a menu:
# o Add a task.
# o View all tasks.
# o Delete a task by index.
# o Mark a task as complete (add "✓" to the task).
# o Exit.
# 3. Keep the program running in a loop until the user exits.
# 4. Validate user input to prevent errors.

def to_do_list():
    tasks = []

    def display_menu():
        print("\nTo-Do List Menu:")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Mark a Task as Complete")
        print("5. Exit")

    def view_tasks():
        if not tasks:
            print("\nYour to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    def add_task():
        task = input("Enter the task you want to add: ").strip()
        if task:
            tasks.append(task)
            print(f"Task added: '{task}'")
        else:
            print("Task cannot be empty.")

    def delete_task():
        view_tasks()
        if tasks:
            try:
                index = int(input("\nEnter the number of the task to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"Task deleted: '{removed_task}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

    def mark_task_complete():
        view_tasks()
        if tasks:
            try:
                index = int(input("\nEnter the number of the task to mark as complete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index] += " ✓"
                    print(f"Task marked as complete: '{tasks[index]}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            print("\nThank you for using the To-Do List program!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the To-Do List program
to_do_list()
