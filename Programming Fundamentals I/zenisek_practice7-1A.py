# Imported the random module:
import random

# All 7 numbers start at 0:
starting_lottery_numbers = [0, 0, 0, 0, 0, 0, 0]

# The loop for generating 7 random numbers:
for generating_num in range(7):
        starting_lottery_numbers[generating_num] = random.randint(0, 9)

# The loop for displaying the generated numbers:
for final_numbers in starting_lottery_numbers:
        print(final_numbers, end="")