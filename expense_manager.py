from datetime import datetime
from file_operations import save_expenses


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
    print(f"Total spent: {total:.2f} €")


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
    print(f"Total spent in {category}: {total:.2f} €")


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
        print(f"{category}: {total:.2f} €")


def display_expenses(expenses):
    for index, expense in enumerate(expenses, start=1):
        print("----------------")
        print(f"{index}. {expense['amount']:.2f} €")
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