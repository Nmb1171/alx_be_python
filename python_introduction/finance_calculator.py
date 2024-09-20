# finance_calculator.py

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings by subtracting expenses from income
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected annual savings with a 5% interest rate
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Output the monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Output the projected savings after one year, including interest
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
