balance = 0

while True:
    print("\n1. Add Income 2. Add Expense 3. Show Balance 4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        amount = float(input("Enter income: "))
        balance += amount
    elif choice == '2':
        amount = float(input("Enter expense: "))
        balance -= amount
    elif choice == '3':
        print("Current Balance:", balance)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
