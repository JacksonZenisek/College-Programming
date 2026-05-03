# Imported the pickle module:
import pickle

# Defined the variables:
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
DISPLAY_ALL = 5
SAVE = 6
LOAD = 7
QUIT = 8

# Defined the main function:
def main():

    vehicles = {}

    user_selection = 0

# The while loop if the user does not select 8 (quit the program):
    while user_selection != QUIT:

        user_selection = get_menu_choice()

        if user_selection == LOOK_UP:
            look_up_lic(vehicles)

        elif user_selection == ADD:
            add_vehicle(vehicles)

        elif user_selection == CHANGE:
            change_vehicle(vehicles)

        elif user_selection == DELETE:
            delete_vehicle(vehicles)

        elif user_selection == DISPLAY_ALL:
            display_all(vehicles)

        elif user_selection == SAVE:
            save_in_dictionary(vehicles)

        elif user_selection == LOAD:
            vehicles = load_the_dictionary()

# Main Menu Display:
def get_menu_choice():
    print()
    print("Vehicles and thier license plate numbers")
    print("-" *40)
    print("1. Look up a license plate number")
    print("2. Add a vehicle and license plate number")
    print("3. Change a license plate number")
    print("4. Delete a vehicle")
    print("5. Display all vehicles")
    print("6. Save Dictionary")
    print("7. Load Dictionary")
    print("8. Quit")
    print()

# Prompts the user to make a choice:
    user_selection = int(input("Enter your choice:"))

# If the user enters a selection that is not between 1-8, the user will get an error:
    while user_selection < LOOK_UP or user_selection > QUIT:
            user_selection = int(input("Enter a valid choice: "))

    return user_selection


# The definitions of all selections:
def look_up_lic(vehicles):

    vehicle = input("Enter the make and model:")

    if vehicle in vehicles:
        print("License Plate:", vehicles[vehicle])
    else:
        print("Vehicle not found.")



def add_vehicle(vehicles):

    vehicle = input("Enter the make and model: ")
    license_plate = input("Enter the license plate number:")

    if vehicle not in vehicles:
        vehicles[vehicle] = license_plate
        print("Vehicle added.")
    else:
        print("That vehicle already exists")



def change_vehicle(vehicles):

    vehicle = input("Enter the make and model: ")

    if vehicle in vehicles:
        license_plate = input("Enter the new license plate:")
        vehicles[vehicle] = license_plate
        print("License plate updated.")
    else:
        print("Vehicle not found.")



def delete_vehicle(vehicles):

    vehicle = input("Enter the make and model: ")

    if vehicle in vehicles:
        del vehicles[vehicle]
        print("Vehicle deleted.")
    else:
        print("Vehicle not found.")


def display_all(vehicles):
    if not vehicles:
        print("No vehicles in dictionary.")
    else:
        print("\nAll Vehicles:")
        for vehicle, license_plate in vehicles.items():
            print(f"{vehicle}: {license_plate}")


def save_in_dictionary(vehicles):
    with open("dictionary.txt", "wb") as file:
        pickle.dump(vehicles, file)

    print("Dictionary saved.")


def load_the_dictionary():
    try:
        with open("dictionary.txt", "rb") as file:
            vehicles = pickle.load(file)

        print("Dictionary loaded.")
        return vehicles

    except FileNotFoundError:
        print("No saved dictionary found.")
        return {}

# Calls the main funtion:
if __name__ == "__main__":
    main()