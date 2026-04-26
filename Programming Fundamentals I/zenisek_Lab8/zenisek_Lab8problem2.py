# Defined the main function:
def main():

# The months of the year in a list:
    months_of_the_year = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]

# Asks the user to input a date:
    date_input = input("Enter a date (mm/dd/yyyy):")

# Separates the month, date, and year with "/":
    month , day , year = date_input.split("/")
    month_num = int(month)
    month_name = months_of_the_year[month_num -1]

# Displays the input date in a different format:
    print(f"{month_name} {int(day)}, {year}")

# Calls the main function:
if __name__ == "__main__":
    main()