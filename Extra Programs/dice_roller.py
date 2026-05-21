# This is an extra program, not part of Programming Fundamentals I!

"""
This program "rolls the dice"! Generates a number between 1 and 6.
"""

# Imported the random module:
import random

# Defined the min and max output values of teh program:
MIN_NUMBER = 1
MAX_NUMBER = 6


#Defined the main function:
def main():

    go_again = "y"

# If user enters "y" or "Y", the program will roll the dice again and will ask the user if they would like to go again:
    while go_again == "y" or go_again == "Y":
        print("Rolling the dice. . . ")
        print(f"You have rolled a {random.randint(MIN_NUMBER, MAX_NUMBER)}")

        go_again = input("Would you like to roll again? (y = yes, n = no)")

# If the user enters "n" or "N", the program will display a closing message:
    if go_again == "n" or go_again =="N":
        print("See you next time!")

# If the program will display an error message and shut down the program:
    else:
        print("Not a valid option, program shutting down.")

# Calls the main function:
main()