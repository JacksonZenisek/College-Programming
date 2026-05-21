# This is an extra program, not part of Programming Fundamentals I!

"""
This program outputs what generation you are based on your birth year.
"""

# Defined the main function:
def main():

    user_input_year = int(input("What year were you born in (1901-2025)?"))
    
# If the user does not enter a birth year between 1901-2025, the program will ask the question again until the user inputs a valid birth year:
    while user_input_year < 1901 or user_input_year > 2025:
        print("That is not a valid year.")
        user_input_year = int(input("What year were you born in (1901-2025)?"))

# Links the input_validation function with the user_input_year parameter:
    input_validation(user_input_year)


# Defined the input_validation function. Will print the output of what generation the user is in:
def input_validation(user_input_year):


    if user_input_year >= 1901 and user_input_year <=1927:
        
        print("You are part of The Greatest Generation")

    elif user_input_year >= 1928 and user_input_year <=1945:

        print("You are part of The Silent Generation")
    
    elif user_input_year >= 1946 and user_input_year <=1964:

        print("You are part of The Boomer Generation")

    elif user_input_year >= 1965 and user_input_year <=1980:
        
        print("You are Generation X")

    elif user_input_year >= 1981 and user_input_year <=1996:

        print("You are part of The Millennials")

    elif user_input_year >= 1997 and user_input_year <=2012:

        print("You are Generation Z")

    elif user_input_year >=2013  and user_input_year <=2025:

        print("You are Generation Alpha")

# Calls the main function:      
main()