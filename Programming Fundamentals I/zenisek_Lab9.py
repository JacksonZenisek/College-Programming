# Defined the main function:
def main():

# Rooms for each course number:
    rooms = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411"
    }

# Instructors for each course:
    instructors = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

# Times for each course:
    times = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m."
    }


    while True:
# Prompts the user to enter the course number:
        input_course = input("Enter a course number or press enter to stop: ")

        if input_course == "":
            break

        input_course = input_course.upper()

# Displays the details of each course number:
        if input_course in rooms:
            print(f"\nThe details for course {input_course} are:")
            print(f"Room: {rooms[input_course]}")
            print(f"Instructor: {instructors[input_course]}")
            print(f"Time: {times[input_course]}\n")
        else:
# Displays an error if the course number is invalid:
            print(f"{input_course} is an invalid course number.\n")

# Calls the main function:
if __name__ == "__main__":
    main()