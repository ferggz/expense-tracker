import json
import os
import csv

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
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def export_to_csv(expenses):
    if not expenses:
        print("No expenses found")
        return

    with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Amount", "Category", "Description", "Date"])

        for expense in expenses:
            writer.writerow([
                expense["amount"],
                expense["category"],
                expense["description"],
                expense["date"]
            ])

    print("Expenses exported to expenses.csv")