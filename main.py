from datetime import datetime
import json
import os

FILE_NAME = "expenses.json"

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

    display_expenses(expenses)

    for expense in expenses:
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

    display_expenses(filtered_expenses)

    for expense in filtered_expenses:
        total += expense["amount"]

    print("----------------")
    print(f"Total spent in {category}: {total} €")


def delete_expense(expenses):
    if not expenses:
        print("No expenses found")
        return

    display_expenses(expenses)

    try:
        choice = int(input("Choose expense number to delete: "))
    except ValueError:
        print("Invalid option")
        return

    if choice < 1 or choice > len(expenses):
        print("Expense not found")
        return

    deleted_expense = expenses.pop(choice - 1)

    save_expenses(expenses)

    print("----------------")
    print("Expense deleted")
    print(f"Deleted: {deleted_expense['description']}")


def edit_expense(expenses):
    if not expenses:
        print("No expenses found")
        return

    display_expenses(expenses)

    try:
        choice = int(input("Choose expense number to edit: "))
    except ValueError:
        print("Invalid option")
        return

    if choice < 1 or choice > len(expenses):
        print("Expense not found")
        return

    expense = expenses[choice - 1]

    new_amount = input(f"New amount ({expense['amount']}): ")
    new_category = input(f"New category ({expense['category']}): ")
    new_description = input(f"New description ({expense['description']}): ")

    if new_amount:
        try:
            expense["amount"] = float(new_amount)
        except ValueError:
            print("Invalid amount")
            return

    if new_category:
        expense["category"] = new_category

    if new_description:
        expense["description"] = new_description

    save_expenses(expenses)

    print("Expense updated")


def show_summary_by_category(expenses):
    if not expenses:
        print("No expenses found")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    print("Summary by category")
    print("----------------")

    for category, total in summary.items():
        print(f"{category}: {total} €")


def display_expenses(expenses):
    for index, expense in enumerate(expenses, start=1):
        print("----------------")
        print(f"{index}. {expense['amount']} €")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Date: {expense['date']}")


def sort_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return

    print("1. Sort by amount")
    print("2. Sort by date")

    choice = input("Choose an option: ")

    if choice == "1":
        sorted_expenses = sorted(
            expenses,
            key=lambda expense: expense["amount"],
            reverse=True
        )

    elif choice == "2":
        sorted_expenses = sorted(
            expenses,
            key=lambda expense: expense["date"],
            reverse=True
        )

    else:
        print("Invalid option")
        return

    display_expenses(sorted_expenses)


def search_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return

    search = input("Search: ").lower()

    matching_expenses = []

    for expense in expenses:
        description = expense["description"].lower()
        category = expense["category"].lower()

        if search in description or search in category:
            matching_expenses.append(expense)

    if not matching_expenses:
        print("No matching expenses found")
        return

    display_expenses(matching_expenses)
    

def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add expense")
        print("2. List expenses")
        print("3. Filter by category")
        print("4. Delete expense")
        print("5. Edit expense")
        print("6. Summary by category")
        print("7. Sort expenses")
        print("8. Search expenses")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            filter_expenses(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            edit_expense(expenses)
        elif choice == "6":
            show_summary_by_category(expenses)
        elif choice == "7":
            sort_expenses(expenses)
        elif choice == "8":
            search_expenses(expenses)
        elif choice == "9":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()