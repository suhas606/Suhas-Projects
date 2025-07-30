tasks = []
while True:
    print("Welcome to To-Do List Application \n")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")   
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"task '{task}' added to the list.")
    elif choice == 2:
        for task in tasks:
            print(task)
    elif choice == 3:
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"task '{task}' removed from the list.")
        else:
            print(f"task '{task}' not found in the list.")
    
    elif choice == 4:
        print("Exiting the application.")
        break