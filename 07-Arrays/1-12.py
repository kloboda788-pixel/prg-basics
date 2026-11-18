# expense category

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

biggest_expense = max(expenses)
category_index = expenses.index(biggest_expense)

print(f'The most expensive category is: {categories[category_index]} ({biggest_expense})')
