# Define the conversion value:
conversion_value = 0.6214

# Define the main function:
def main():
# The user enters the distance in kilometers (km), then calls the conversion function:
    user_km_input = float(input("Enter a distance in Kilometers (km):"))
    conversion_operation(user_km_input)

# Define the conversion function, then the conversion from kilometers to miles happens. The output in miles is then displayed in two decimal form for simplicity:
def conversion_operation(user_km_input):
    output_miles = user_km_input * conversion_value
    print(f"The distance in miles is: {output_miles:.2f}")

# The program calls the main definition to display the user questionare:
main()
