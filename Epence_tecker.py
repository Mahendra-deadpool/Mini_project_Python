expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append((amount, category))
    print("Expense added.")

def view_expenses():
    total = 0
    for amount, category in expenses:
        print(f"{category}: ₹{amount}")
        total += amount
    print(f"Total spent: ₹{total}")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid option.")
