budget = 5000  # Weekly Budget - constant variable so I made it globally.


def get_expenses_per_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    expenses = []

    for day in days:
        amount = float(input(f"Enter your expense for {day}: "))
        expenses.append(amount)

    return sum(expenses), expenses


def main():
    total_expense, daily_expenses = get_expenses_per_day()
    remaining_budget = budget - total_expense

    # Display results
    print("\nDaily Expenses:")
    for day, expense in zip(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                            daily_expenses):
        print(f"{day}: {expense:.2f}")

    print(f"\nTotal Expense: {total_expense:.2f}")
    print(f"Remaining Budget: {remaining_budget:.2f}")

    # Check if within budget
    if total_expense > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print("Good job! You are within your budget.")


main()
