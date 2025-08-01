expenses = []
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Remove Expense")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        item = input("enter the item : ")
        cost = float(input("enter the cost : "))
        expenses.append((item, cost))
        print(f"Expense '{item}' added with cost {cost}.")
    elif choice == 2:
        for item,cost in expenses:
            print(f"Item: {item}, Cost: {cost}")
    elif choice == 3:
        item = input("Enter the item to remove: ")
        cost = float(input("Enter the cost to remove: "))
        if (item, cost) in expenses:
            expenses.remove((item, cost))
            print(f"Expense '{item}' removed.")
        else:
            print("Expense not found.")
    elif choice == 4:
        print("Exiting the application.")
        break