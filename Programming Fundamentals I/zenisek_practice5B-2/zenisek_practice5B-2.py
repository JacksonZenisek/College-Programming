# I imported random and square.py nodes to this file:
import random
import square

# Defines the main function, generates a number between 1 - 100 that will act as a side of the square:
def main():
    side = random.randint(1, 100)
    
# Defines the variables that will linked to the calculation functions in square.py:
    area = square.square_area(side)
    perimeter = square.square_perimeter(side)


# Prints the output of the randomly generated side, the calculated area of the square based on the given length of the side, and the total perimeter of the square:
    print(f"Side:{side:,.0f}")
    print(f"Area:{area:,.0f}")
    print(f"Perimeter: {perimeter:,.0f}")

# Returns the main function:
main()