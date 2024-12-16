#Get the user's monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
#Calculate the user's monthly savings
monthly_savings = monthly_income - monthly_expenses

#Calculate projected annual savings
annual_interest_rate = 0.05
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

#Print the monthly savings and projected annual savings
print(f"Your monthly savings are: ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_annual_savings)}.")
