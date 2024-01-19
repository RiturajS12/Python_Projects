class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def view_expenses(self):
        [print(f"{i+1}. Amount: ${e['amount']}, Category: {e['category']}") for i, e in enumerate(self.expenses)]

    def view_spending_pattern(self, category=None):
        expenses = [e['amount'] for e in self.expenses if not category or e['category'] == category]
        print(f"Total spending in '{category}': ${sum(expenses)}" if category else f"Total spending: ${sum(expenses)}")


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracking System:\n1. Add Expense\n2. View Expenses\n3. View Spending Pattern\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount, category = float(input("Enter the expense amount: $")), input("Enter the expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully!")

        elif choice == '2':
            print("\nAll Expenses:"), tracker.view_expenses()

        elif choice == '3':
            category = input("Enter the category to view spending pattern (leave blank for overall): ")
            tracker.view_spending_pattern(category)

        elif choice == '4':
            print("Exiting Expense Tracking System. Goodbye!"), exit()

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
