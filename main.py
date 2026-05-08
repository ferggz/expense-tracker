from datetime import datetime
import json
import os

FILE_NAME = "expenses.json"

print("1. Add expense")
print("2. List expenses")
print("3. Filter by category")
print("4. Exit")

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount")
        return

    category = input("Category: ")
    description = input("Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added")


def list_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return

    total = 0

    for expense in expenses:
        print("----------------")
        print(f"Amount: {expense['amount']} €")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Date: {expense['date']}")

        total += expense["amount"]

    print("----------------")
    print(f"Total spent: {total} €")


def filter_expenses(expenses):
    category = input("Enter category: ")

    filtered_expenses = []

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            filtered_expenses.append(expense)

    if not filtered_expenses:
        print("No expenses found")
        return

    total = 0

    for expense in filtered_expenses:
        print("----------------")
        print(f"Amount: {expense['amount']} €")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Date: {expense['date']}")

        total += expense["amount"]

    print("----------------")
    print(f"Total spent in {category}: {total} €")


def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add expense")
        print("2. List expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            filter_expenses(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()