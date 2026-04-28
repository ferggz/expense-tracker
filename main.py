import json

expenses = []

def main():
    while True:
        print("1. Add expense")
        print("2. List expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            description = input("Description: ")

            expense = {
                "amount": amount,
                "category": category,
                "description": description
            }

            expenses.append(expense)

            print("Expense added")

        elif choice == "2":
            print("List expenses")
        elif choice == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()