# Simple To-Do List Application

# Each task contains its name and its status
tasks = []

while True:
    print("\nTo-Do List Menu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Update a task")
    print("4. Mark a task as completed")
    print("5. Delete a task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task_name = input("Enter the task: ")
        tasks.append([task_name, "Pending"])
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i][0], "-", tasks[i][1])

    elif choice == "3":
        task_number = int(input("Enter the task number to update: "))
        if task_number >= 1 and task_number <= len(tasks):
            new_name = input("Enter the updated task: ")
            tasks[task_number - 1][0] = new_name
            print("Task updated.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        task_number = int(input("Enter the task number to complete: "))
        if task_number >= 1 and task_number <= len(tasks):
            tasks[task_number - 1][1] = "Completed"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        task_number = int(input("Enter the task number to delete: "))
        if task_number >= 1 and task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
