# User input questionares:
monthly_gross_income_inp = float(input("What is your gross monthly income?:"))
monthly_deductions = float(input("What are your monthly deductions?:"))

# Calculations of total monthly net income, yearly gross pay, and yearly net pay
total_monthly_income = monthly_gross_income_inp - monthly_deductions
yearly_gross_pay = monthly_gross_income_inp * 12
yearly_net_pay = yearly_gross_pay - (monthly_deductions * 12)

# Outputs of the 3 inputs and calculations
print(f"Your monthly net income is:${total_monthly_income:,.2f}")
print(f"Your yearly gross income is:${yearly_gross_pay:,.2f}")
print(f"Your yearly net income is:${yearly_net_pay:,.2f}")