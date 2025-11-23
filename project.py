tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return

    task_num = input("Enter the task number to delete: ")

    if task_num.isdigit():
        index = int(task_num) - 1

        if index >= 0 and index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")


while True:
    print("\nMenu:")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 4.")
