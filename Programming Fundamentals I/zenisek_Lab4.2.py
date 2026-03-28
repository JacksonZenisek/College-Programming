# Jackson Zenisek
# Complete
"""
The program's purpose is to calulate the rise of the ocean level in the next 25 years, given that the ocean rises 1.8 millimeters/year.
The program will display the year and the rise amount.
"""

print("Year\tRise (in millimeters)")
print("--------------------------")

# Setting the starting ocean rise at 1.80mm starting at year 1:
ocean_level_gain = 1.8

# Setting the loop, in which the range of the year will start at 1 and end at 25.
for year_number in range (1, 26):
        print(f"{year_number} \t {ocean_level_gain:.2f}")

# The ocean level will rise 1.8mm per year passed.
        ocean_level_gain = ocean_level_gain + 1.8
