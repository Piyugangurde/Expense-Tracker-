expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Total")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g. Food, Travel): ")
        expenses.append({'amount': amount, 'category': category})
        print("Expense added!")

    elif choice == 2:
        total = sum([e['amount'] for e in expenses])
        print(f"Total Expense: ₹{total}")

    elif choice == 3:
        print("Bye!")
        break

    else:
        print("Invalid choice.")