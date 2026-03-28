# Jackson Zenisek
# Complete
"""
This program calculates the total discount amount, and the total amount baed on the amount of software packages purchased with the users input.
It is labeled with the dollar sign and rounds to the nearest two decimal places.
"""

# User is asked how many packages were purchased:
number_of_purchases_packages = int(input("Enter the number of packages purchased?"))

# The calculation before discount amount:
value_before_discount = number_of_purchases_packages * 149


# The selected discount based on the user's input. Ex: User inputs 10 were purchased, so it calculates the 10% discount, followed by the total amount after applied discount.
# If the input value is a negative nukber, then the program prints "Invalid number", and exits the program.
if number_of_purchases_packages < 0:
    print("Invalid number.")
    exit()

if number_of_purchases_packages <10:
    sales_discount = 0

elif number_of_purchases_packages >=10 and number_of_purchases_packages <=49 :
    sales_discount = value_before_discount * 0.10

elif number_of_purchases_packages >=50 and number_of_purchases_packages <=99:
    sales_discount = value_before_discount * 0.20

elif number_of_purchases_packages >=100 and number_of_purchases_packages <=149:
    sales_discount = value_before_discount * 0.30

else:
    sales_discount = value_before_discount * 0.40


# The calculation of the total sales discount
total_sale_amount = value_before_discount - sales_discount

6
# The total amount is displayed regardless of the amount of software packages purchased, and the amount discounted.
print(f"Discount Amount:${sales_discount:,.2f}")
print(f"Total Amount:${total_sale_amount:,.2f}")