
task_list = []

def add_task():
    task = input("Add Task: ")
    task_list.append(task)
    save_tasks()

def view_tasks():
    for index, task in enumerate(task_list):
        print(f"{index} - {task}")

def update_task():
    old_task = int(input("Task ID: "))
    if old_task < len(task_list):
        new_task = input("Update Task: ")
        task_list[old_task] = new_task
    save_tasks()
    return new_task

def delete_task():
    task = int(input("Task ID: "))
    if task <  len(task_list):
        del task_list[task]
    save_tasks()

def save_tasks():
    with open('todo.txt', 'w') as f:
        f.write('\n'.join(task_list))

def load_tasks():
    with open('todo.txt', 'r') as f:
        tasks = f.read().splitlines()
    task_list.extend(tasks)
    
def main():
    try:
        load_tasks()
    except FileNotFoundError:
        return task_list

    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()
