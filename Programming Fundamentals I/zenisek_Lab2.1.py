#Jackson Zenisek
#Complete
"""
My program receives the number of servings of spaghetti sauce that the user wants to make by the user's input.
The process multiplies each ingredient by the number of servings that the user wants divided by 4, as the amounts of each ingredient is used to make 4 servings by default.
The output displays the amount of each ingredient that is needed to produce the desired serving amount from the user.
"""

# Servings amount question:
servings_value_question = int(input("Enter the number of servings of spaghetti sauce you want to make:"))


# Listed values per item:
new_servings_value = servings_value_question / 4

cups_of_tomato_sauce = 2

cups_of_tomato_paste = .333

cloves_garlic = 2

tablespoon_oregano = 1


# Calculations of each ingredient:
total_cups_of_tomato_sauce = cups_of_tomato_sauce * new_servings_value

total_cups_of_tomato_paste = cups_of_tomato_paste * new_servings_value

total_cloves_garlic = cloves_garlic * new_servings_value

total_tablespoon_oregano = tablespoon_oregano * new_servings_value


# Output of the amount of ingredients:
print("To make" ,(f"{servings_value_question:.1f} servings of spaghetti sauce, you will need:"))
print((f"{total_cups_of_tomato_sauce:.2f} cups of tomato sauce"))
print((f"{total_cups_of_tomato_paste:.2f} cups of tomato paste"))
print((f"{total_cloves_garlic:.2f} cloves of garlic"))
print((f"{total_tablespoon_oregano:.2f} tablespoons of oregano"))
