# Imported math. I didn't need this python library for this specific program, however it is still good to have:
import math

"""
This program presents a list of distance calculations that you may perform. Once you select a calculation, 
enter the unit of distance that you already have and the program converts it to your desried distance.
"""


# Defined the main function:
def main():
        
# Displays the header of the Option Menu:
        print(f"\nOption Menu")
        print("-" *25)

# Displays the 8 availible selections:
        select_option = int(input("Enter 1 for inches to feet\nEnter 2 for feet to yards\nEnter 3 for cm to inches\nEnter 4 for mm to inches\nEnter 5 for feet to miles\nEnter 6 for yards to miles\nEnter 7 for meters to miles\nEnter 8 for meters to kilometers\nEnter option here:"))

# The selected menu director:
        if select_option == 1:
             option1()

        elif select_option == 2:
             option2()

        elif select_option == 3:
             option3()

        elif select_option == 4:
             option4()

        elif select_option == 5:
             option5()

        elif select_option == 6:
             option6()

        elif select_option == 7:
             option7()

        elif select_option == 8:
             option8()

# The option menu error handler:
        else:
             print("\nError: Invalid option, please try again.\n")

             print(f"\nOption Menu")
             print("-" *25)
             select_option = int(input("Enter 1 for inches to feet\nEnter 2 for feet to yards\nEnter 3 for cm to inches\nEnter 4 for mm to inches\nEnter 5 for feet to miles\nEnter 6 for yards to miles\nEnter 7 for meters to miles\nEnter 8 for meters to kilometers\nEnter option here:"))


# The definitions of all 8 availible calculations:
def option1():
      
    inches =  float(input("Enter inches:"))

    feet = inches / 12

    print(f"{inches} inches is {feet:,.2f} feet.\n")

    go_again()

def option2():
      
    feet =  float(input("Enter feet:"))

    yards = feet / 3

    print(f"{feet} feet is {yards:,.2f} yards.")

    go_again()

def option3():
     
     centimeters = float(input("Enter cm:"))

     inches = centimeters / 2.54
     
     print(f"{centimeters} centimeters is {inches:,.2f} inches.")

     go_again()

def option4():

     millimeters = float(input("Enter mm:"))

     inches = millimeters / 25.4
     
     print(f"{millimeters} millimeters is {inches:,.2f} inches.")

     go_again()

def option5():

     feet = float(input("Enter feet:"))

     miles = feet / 5280

     print(f"{feet} feet is {miles:,.2f} miles.")

     go_again()

def option6():

     yards = float(input("Enter yards:"))

     miles = yards / 1760

     print(f"{yards} yards is {miles:,.2f} miles.")

     go_again()

def option7():

     meters = float(input("Enter meters:"))

     miles = meters / 1609.344

     print(f"{meters} meters is {miles:,.2f} miles.")

     go_again()

def option8():

     meters = float(input("Enter meters:"))

     kilometers = meters / 1000

     print(f"{meters} meters is {kilometers:,.2f} kilometers.")

     go_again()

# The go again? questionare:

def go_again():

     try_again_questionare = str(input("Would you like to perform another calculation? (y = yes, n = no):"))

     if try_again_questionare == "y" or try_again_questionare == "Y":

      main()

     elif try_again_questionare == "n" or try_again_questionare == "N":
          print("\nSee you next time!")
          exit()

     else:
          print("\nInvalid option, program shutting down.")
          exit()

# Calls the main function:
if __name__ == "__main__":
    main()