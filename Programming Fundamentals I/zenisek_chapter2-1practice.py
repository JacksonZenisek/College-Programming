"""
The purpose of this program is to calculate the total cost of hamburger, fires, and shake given the user's input.
This program also calculates the average cost of the meal.
"""

# The questionares of the cost of each food item:
cost_of_hamburger = float(input("What is the cost for the hamburger?:"))
cost_of_fries = float(input("What is the cost for the fries?:"))
cost_of_shake = float(input("What is the cost for the shake?:"))

# The calculations for the total cost of the meal based on the user's input, and the average cost of the meal.

total_user_cost = cost_of_hamburger + cost_of_fries + cost_of_shake

average_meal_cost = total_user_cost / 3

# The output based on the user's input with the questionare, and the calculations of both the total input costs of the hamburger, fires, and shake. As well as the average cost of the meal.

print(f"The cost is: ${total_user_cost:.2f}")
print(f"The average cost is: ${average_meal_cost:.2f}")