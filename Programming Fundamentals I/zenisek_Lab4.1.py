# Jackson Zenisek
# Complete
"""
This program asks the user to input the amount of money in which the user is attempting to budget throughout the month.
The loop allows the user to input specific values of money spend over the duration of the month, and the program adds all values together to list the sum of those values.
If the total sum of all input values is less than the targeted budget, then the program will list how much the user is over budget followed by a custom message.
"""

# Asks the user the targeted monthly budget:
targeted_monthly_budget = float(input("Enter amount budgeted for the month: "))

# From the start, the total amount spent is equal to 0 until the value changes:
total_amount_spent = 0

# Asks the user to input the amount spend:
monthly_expenses = float(input("Enter an amount spent (0 to quit): "))

# As long as thge input value doesn't equal to 0, the loop will continue. When the user is done with the expenses amounts, the user inputs 0 to end the loop and proceed with the final outputs:
while monthly_expenses !=0:
    total_amount_spent += monthly_expenses
    monthly_expenses = float(input("Enter an amount spent (0 to quit): "))

# The program then prints the output values of both the targeted montly budget, and the sum of the all monthly expenses:
print(f"Budgeted: ${targeted_monthly_budget:,.2f}")
print(f"Spent: $ {total_amount_spent:,.2f}")

# The calculation of the total amount spent - the targeted monthly budget that determines the final message:
final_subtraction = total_amount_spent - targeted_monthly_budget

# If the final subtraction value is less than 0, meaning that the user went over budget, then the program will list how much money the user went over budget followed by a short message:
if final_subtraction > 0:
    print(f"You are $ {final_subtraction:,.2f} over budget. PLAN BETTER NEXT TIME!")
