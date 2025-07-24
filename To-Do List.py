tasks = []

def show_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted.")
    else:
        print("Invalid number.")

while True:
    print("\n1. Add Task  2. Delete Task  3. View Tasks  4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid option.")
