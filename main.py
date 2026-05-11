from file_operations import (
    load_expenses,
    export_to_csv
)

from expense_manager import (
    add_expense,
    list_expenses,
    filter_expenses,
    delete_expense,
    edit_expense,
    show_summary_by_category,
    sort_expenses,
    search_expenses
)


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
        print("9. Export to CSV")
        print("10. Exit")

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
            export_to_csv(expenses)
        elif choice == "10":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()