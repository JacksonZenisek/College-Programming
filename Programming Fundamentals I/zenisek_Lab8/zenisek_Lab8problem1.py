# Defined the main function:
def main():
    try:

# Reads text.txt:
        file_open = open("text.txt", "r")
        file_contents = file_open.read()
        file_open.close()

# Defined the variables for uppercase, lowercase, digits, and spaces:
        uppercase = 0
        lowercase = 0
        digits = 0
        blank_spaces = 0

# Listed the conditions:
        for ch in file_contents:

            if ch.isupper():
                uppercase += 1
            
            elif ch.islower():
                lowercase += 1

            elif ch.isdigit():
                digits += 1
            
            elif ch.isspace():
                blank_spaces += 1

# Displays the outputs:
        print("Uppercase letters:", uppercase)
        print("Lowercase letters:", lowercase)
        print("Digits:", digits)
        print("Spaces:", blank_spaces)

# Error handler is the text file cannot be read:
    except IOError:
        print("Error: Could not open file.")

# Calls the main function:
if __name__ == "__main__":
    main()