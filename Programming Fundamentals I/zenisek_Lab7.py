# Jackson Zenisek
# Complete
"""
This program allows a user to enter 10 numbers that will bne organized into a list, and another number to see what numbers from the list are greater than
the number entered. The program then displays all 10 entered list numbers from the beginning of the program, and the numbers that are greater than the selected number.
"""


# Defined the main function:
def main():

#The numbers the user inputs to the program will be organized in a list:
    input_numbers = []

    print("Enter a list of 10 integers:")

# Prompts the user to enter 10 numbers:
    for i in range(10):
        num = int(input("Enter a number:"))
        input_numbers.append(num)

    n = int(input("Enter the number you wish to test if the list elements aree greater than: "))

    display_larger(input_numbers, n)

def display_larger(input_numbers, n):
    greater_numbers = []

# The loop that determines which entered numbers are greater than the selected number:
    for num in input_numbers:
        if num > n:
            greater_numbers.append(num)
    
# Displays the output of all 10 entered numbers in a list, and displays the numbers in another list that are greater than the selected number:
    print("\nNumber:" , n)
    print("List of numbers:")
    print(input_numbers)
    print("List of numbers that are larger than", n, ":")
    print(greater_numbers)

# Calls the main function:
if __name__ == "__main__":
    main()
