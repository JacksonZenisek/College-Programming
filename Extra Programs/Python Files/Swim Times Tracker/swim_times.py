# Imported date from datetime library to keep the date user-friendly:
from datetime import date


# Defined the main function:
def main():

# The first thing that the program asks:
    write_or_read = int(input("Main Menu:\n1) Enter swim times\n2) View swim times\nEnter Here:"))

    if write_or_read == 1:
        enter_times_main_menu()

    elif write_or_read == 2:
        read_times()

# Error handlers for main menu:
    else:
        print("\nInvalid option, please try again.")

        write_or_read = int(input("Main Menu:\n1) Enter swim times\n2) View swim times\nEnter Here:"))

        if write_or_read == 1:
            enter_times_main_menu()

        elif write_or_read == 2:
            read_times()

        else:
            print("\nInvalid option, program shutting down.")

# Function for the read times menu:
def read_times():

    open_butterfly = open("butterfly_times_capture.txt" , "r")

    open_backstroke = open("backstroke_times_capture.txt" , "r")

    open_breaststroke = open("breaststroke_times_capture.txt" , "r")

    open_freestyle = open("freestyle_times_capture.txt" , "r")

    open_IM = open("IM_times_capture.txt" , "r")

    select_what_to_read = int(input("\nWhat times do you want to view?\n1) Butterfly\n2) Backstroke\n3) Breaststroke\n4) Freestyle\n5) IM\nEnter here:"))

    if select_what_to_read == 1:
        read_butterflyfile = open_butterfly.read()
        print(read_butterflyfile)

    elif select_what_to_read == 2:
        read_backstrokefile = open_backstroke.read()
        print(read_backstrokefile)

    elif select_what_to_read == 3:
        read_breaststrokefile = open_breaststroke.read()
        print(read_breaststrokefile)

    elif select_what_to_read == 4:
        read_freestyle = open_freestyle.read()
        print(read_freestyle)

    elif select_what_to_read == 5:
        read_IM = open_IM.read()
        print(read_IM)

    else:
        print("\nInvalid option, pelase try again.")

        select_what_to_read = int(input("\nWhat times do you want to view?\n1) Butterfly\n2)Backstroke\n3)Breaststroke\n4)Freestyle5)\nIM\nEnter here:"))


# Function for the enter times menu:
def enter_times_main_menu():

    select_stroke = int(input("\nWhat stroke did you swim?:\n1) Butterfly\n2) Backstroke\n3) Breaststroke\n4) Freestyle\n5) IM\nEnter here:"))

    if select_stroke == 1:
        Butterfly(select_stroke)

    elif select_stroke == 2:
        Backstroke(select_stroke)

    elif select_stroke == 3:
        Breaststroke(select_stroke)

    elif select_stroke == 4:
        Freestyle(select_stroke)

    elif select_stroke == 5:
        IM(select_stroke)

    else:
        print("Invalid option, pelase try again.")

        select_stroke = int(input("What stroke did you swim?:\n1) Butterfly\n2) Backstroke\n3) Breaststroke\n4) Freestyle\n5) IM\nEnter here:"))

# Function for the Butterfly times inputs:
def Butterfly(stroke):

    todays_date = date.today()

    event_select = int(input("\nEnter the event:\n1) 50m Butterfly\n2) 100m Butterfly\n3) 200m Butterfly\nEnter here:"))

    if event_select == 1:
        
        open_file = open("butterfly_times_capture.txt" , "a")

        open_file.write("50m Butterfly" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to butterfly_times_capture.txt")

        enter_more_times()

    if event_select == 2:
        
        open_file = open("butterfly_times_capture.txt" , "a")

        open_file.write("100m Butterfly" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to butterfly_times_capture.txt")

        enter_more_times()

    if event_select == 3:
        
        open_file = open("butterfly_times_capture.txt" , "a")

        open_file.write("200m Butterfly" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to butterfly_times_capture.txt")

        enter_more_times()

# Function for the Backstroke times inputs:
def Backstroke(stroke):

    todays_date = date.today()

    event_select = int(input("\nEnter the event:\n1) 50m Backstroke\n2) 100m Backstroke\n3) 200m Backstroke\nEnter here:"))

    if event_select == 1:
        
        open_file = open("backstroke_times_capture.txt" , "a")

        open_file.write("50m Backstroke" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to backstroke_times_capture.txt")

        enter_more_times()

    if event_select == 2:
        
        open_file = open("backstroke_times_capture.txt" , "a")

        open_file.write("100m Backstroke" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to backstroke_times_capture.txt")

        enter_more_times()

    if event_select == 3:
        
        open_file = open("backstroke_times_capture.txt" , "a")

        open_file.write("200m Backstroke" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to backstroke_times_capture.txt")

        enter_more_times()


# Function for the Breaststroke times inputs:
def Breaststroke(stroke):

    todays_date = date.today()

    event_select = int(input("\nEnter the event:\n1) 50m Breaststroke\n2) 100m Breaststroke\n3) 200m Breaststroke\nEnter here:"))

    if event_select == 1:
        
        open_file = open("breaststroke_times_capture.txt" , "a")

        open_file.write("50m Breaststroke" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to breaststroke_times_capture.txt")

        enter_more_times()

    if event_select == 2:
        
        open_file = open("breaststroke_times_capture.txt" , "a")

        open_file.write("100m Breaststroke" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to breaststroke_times_capture.txt")

        enter_more_times()

    if event_select == 3:
        
        open_file = open("breaststroke_times_capture.txt" , "a")

        open_file.write("200m Breaststroke" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to breaststroke_times_capture.txt")

        enter_more_times()


# Function for the Freestyle times inputs:
def Freestyle(stroke):

    todays_date = date.today()

    event_select = int(input("\nEnter the event:\n1) 50m Freestyle\n2) 100m Freestyle\n3) 200m Freestyle\n4) 400m Freestyle\n5) 800m Freestyle\n6) 1650m Freestyle\nEnter here:"))

    if event_select == 1:
        
        open_file = open("freestyle_times_capture.txt" , "a")

        open_file.write("50m Freestyle" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to freestyle_times_capture.txt")

        enter_more_times()


    if event_select == 2:
        
        open_file = open("freestyle_times_capture.txt" , "a")

        open_file.write("100m Freestyle" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to freestyle_times_capture.txt")

        enter_more_times()

    if event_select == 3:
        
        open_file = open("freestyle_times_capture.txt" , "a")

        open_file.write("200m Freestyle" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to freestyle_times_capture.txt")

        enter_more_times()

    if event_select == 4:
        
        open_file = open("freestyle_times_capture.txt" , "a")

        open_file.write("400m Freestyle" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to freestyle_times_capture.txt")

        enter_more_times()

    if event_select == 5:
        
        open_file = open("freestyle_times_capture.txt" , "a")

        open_file.write("800m Freestyle" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to freestyle_times_capture.txt")

        enter_more_times()

    if event_select == 6:
        
        open_file = open("freestyle_times_capture.txt" , "a")

        open_file.write("1650m Freestyle" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to freestyle_times_capture.txt")

        enter_more_times()

# Function for IM inputs:
def IM(stroke):

    todays_date = date.today()

    event_select = int(input("\nEnter the event:\n1) 200m IM\n2) 400m IM\nEnter here:"))

    if event_select == 1:
        
        open_file = open("IM_times_capture.txt" , "a")

        open_file.write("200m IM" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to IM_times_capture.txt")

        enter_more_times()

    if event_select == 2:
        
        open_file = open("IM_times_capture.txt" , "a")

        open_file.write("400m IM" + "\n")

        time_entry = (input("What was your time?(mm:sss.ms)"))

        open_file.write(f"Time:\t{time_entry}" + "\n")

        open_file.write(f"Date:\t{todays_date}" + "\n\n")

        print("\nEvent, time, and date have been recorded to IM_times_capture.txt")

        enter_more_times()

# Function for enter more times:
def enter_more_times():

    enter_more_times_questionare = str(input("\nWould you like to enter more times? (y = yes, n = no):"))

    if enter_more_times_questionare == "y" or enter_more_times_questionare == "Y":
        
        enter_times_main_menu()

# If the user inputs no, they are displayed a message:
    elif enter_more_times_questionare == "n" or enter_more_times_questionare == "N":
        print("See you after your next swim!")

# If the user inputs something other than yes or no, they are displayed with a different message:
    else:
        print("Invalid option, program shutting down.")


if __name__ == "__main__":
    main()