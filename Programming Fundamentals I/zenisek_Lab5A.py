# Jackson Zenisek
# Complete
"""
This program asks ratings from 5 critics to rate a resturant. Once all 5 ratings have been given by the critics,
the program divides the sum of all 5 ratings by 5 to output the average ratings, along with the number of stars given the average output.
"""

# Define the "main" function:
def main():

# The critic rating total score starts at 0:
    critic_ratings_total = 0

# This for loop places the critics in a range mode, starting from critic 1 and ending with critic 5:
    for criticnum in range(1,6):
        while True:
            user_rating = float(input(f"Critic {criticnum}, please enter your rating (0-10):"))

# Input validation section. This will verify that the user is entering a rating from 1 - 10:
            if user_rating < 0 or user_rating > 10:
                print("Error: rating must be between 0 - 10.")
            else:
                critic_ratings_total += user_rating
                break

# This operation divides all 5 ratings by 5:
    average_of_all_ratings = critic_ratings_total / 5

# This is the output message that displays the average rating in decimal, and in star format:
    print(f"Your average rating of {average_of_all_ratings:.1f} gives you {output_stars(average_of_all_ratings)}")


# Define the output_stars function that allows the program to output the star rating based on the 5 critics average score:
def output_stars(average):
    if average > 9:
        return("*****")
    elif average >= 8:
        return("****")
    elif average >= 7:
        return("***")
    elif average >= 6:
        return("**")
    elif average >=5:
        return("*")
    else:
        return("No Stars")
    
# Return the main function that runs the entire program:
main()