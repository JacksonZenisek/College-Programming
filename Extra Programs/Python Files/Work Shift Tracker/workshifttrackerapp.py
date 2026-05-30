# Developer: Jackson Zenisek

# APPLICATION EDITION

"""
This program displays the current shift working at my company. We have A, B, C, and D shifts. 
When you run the program, it will display the current shift given this schedule:

Short Week:
Sunday - Tuesday 6:00am = 6:00pm = A shift
Sunday - Tuesday 6:00pm = 6:00am = C shift
Wednesday - Saturday 6:00am = 6:00pm = B shift
Wednesday - Saturday 6:00pm = 6:00am = D shift

Long Week:

Sunday - Tuesday 6:00am = 6:00pm = A shift
Sunday - Tuesday 6:00pm = 6:00am = C shift
Wednesday - Saturday 6:00am = 6:00pm = B shift
Wednesday - Saturday 6:00pm = 6:00am = D shift


Note: Short weeks are weeks that A and C shift don't work on Wednesdays. Long weeks are weeks that A and C shift do work on Wednesdays.
"""


# Imported needed modules the date and time, and the GUI Window: 
import datetime
import turtle


# Defined the main function:
def main():

        
# Gets the local real time:
    now = datetime.datetime.now()
    today = now.date()

# Defines the week and time associated with the real time variable:
    current_day = now.weekday()
    current_time = now.time()

    day_start = datetime.time(6, 0, 0)
    day_end = datetime.time(17, 59, 59)
    night_start = datetime.time(18, 0, 0)

    current_week = now.isocalendar().week
    reference_date = datetime.date(2026, 5, 6)


    weeks_passed = (today - reference_date).days // 7


# The calculations for alternating Wednesdays:
    b_and_d_week = weeks_passed % 2 == 0
    a_and_c_week = not b_and_d_week


# Determines the printed week schedule based on which shifts work 4 days of that week:
    if b_and_d_week:
        weekly_schedule = "This week's schedule:\n\nA Shift = Sunday - Tuesday (6am - 6pm)\nC Shift = Sunday - Tuesday (6pm - 6am)\n-------------------------------------------\n" + "B Shift = Wednesday - Saturday (6am - 6pm)\nD Shift = Wednesday - Saturday (6pm - 6am)"

    elif a_and_c_week:
        weekly_schedule = "This week's schedule:\n\nA Shift = Sunday - Wednesday (6am - 6pm)\nC Shift = Sunday - Wednesday (6pm - 6am)\n-------------------------------------------\n" + "B Shift = Thursday - Saturday (6am - 6pm)\nD Shift = Thursday - Saturday (6pm - 6am)"


# The day and time that determines which shift is currently working:
# The time method that displays the day of the week, the date, and the time (12hr clock):


# A shift conditions:
    if current_day in (6, 0, 1) or (current_day == 2 and a_and_c_week):
            if day_start <= current_time <= day_end:
                shift = "Current shift is: A Shift\n"
                upcoming_shift = "Next shift: C Shift, starts at 6:00pm"
                time = now.strftime("%A, %B, %d, %Y | %I:%M:%S %p")
                time_highlight()
                a_highlight()
                upcoming_sched_highlighter()
                word_layout(shift,time,weekly_schedule,upcoming_shift)
                print(now)

# C Shift Conditions:
            else:
                shift = "Current shift is: C Shift\n"
                upcoming_shift = "Next shift: A Shift, starts at 6:00am"
                time = now.strftime("%A, %B, %d, %Y | %I:%M:%S %p")
                time_highlight()
                c_highlight()
                upcoming_sched_highlighter()
                word_layout(shift,time,weekly_schedule,upcoming_shift)
                print(now)
                
# B Shift Conditions:
    elif current_day in (3, 4, 5) or (current_day == 2 and b_and_d_week):
            if day_start <= current_time <= day_end:
                shift = "Current shift is: B Shift\n"
                upcoming_shift = "Next shift: D Shift, starts at 6:00pm"
                time = now.strftime("%A, %B, %d, %Y | %I:%M:%S %p")
                time_highlight()
                b_highlight()
                upcoming_sched_highlighter()
                word_layout(shift,time,weekly_schedule,upcoming_shift)
                print(now)

# D Shift Conditions:
            else:
                 shift = "Current shift is: D Shift\n"
                 upcoming_shift = "Next shift: B Shift, starts at 6:00am"
                 time = now.strftime("%A, %B, %d, %Y | %I:%M:%S %p")
                 time_highlight()
                 d_highlight()
                 upcoming_sched_highlighter()
                 word_layout(shift,time,weekly_schedule,upcoming_shift) 
                 print(now)

#------------------PRIMARY CODE SECTION----------------------------
#------------------GUI INTERFACE SECTION---------------------------


# The highlighter for A shift (Red):
def a_highlight():

    highlighterashift = turtle.Turtle()
    highlighterashift.hideturtle()
    highlighterashift.penup()
    highlighterashift.goto(-180, 180)
    highlighterashift.pendown()
    highlighterashift.color("red")
    highlighterashift.begin_fill()

    for _ in range(2):

        highlighterashift.forward(360)
        highlighterashift.right(90)
        highlighterashift.forward(60)
        highlighterashift.right(90)
    highlighterashift.end_fill()



# The highlighter for B shift (Green):
def b_highlight():

    highlighterbshift = turtle.Turtle()
    highlighterbshift.hideturtle()
    highlighterbshift.penup()
    highlighterbshift.goto(-180, 180)
    highlighterbshift.pendown()
    highlighterbshift.color("green")
    highlighterbshift.begin_fill()

    for _ in range(2):

        highlighterbshift.forward(360)
        highlighterbshift.right(90)
        highlighterbshift.forward(60)
        highlighterbshift.right(90)
    highlighterbshift.end_fill()


# The highlighter for C shift (Yellow):
def c_highlight():

    highlightercshift = turtle.Turtle()
    highlightercshift.hideturtle()
    highlightercshift.penup()
    highlightercshift.goto(-180, 180)
    highlightercshift.pendown()
    highlightercshift.color("yellow")
    highlightercshift.begin_fill()

    for _ in range(2):

        highlightercshift.forward(360)
        highlightercshift.right(90)
        highlightercshift.forward(60)
        highlightercshift.right(90)
    highlightercshift.end_fill()



# The highlighter for D shift (Blue):
def d_highlight():

    highlighterdshift = turtle.Turtle()
    highlighterdshift.hideturtle()
    highlighterdshift.penup()
    highlighterdshift.goto(-180, 180)
    highlighterdshift.pendown()
    highlighterdshift.color("blue")
    highlighterdshift.begin_fill()

    for _ in range(2):

        highlighterdshift.forward(360)
        highlighterdshift.right(90)
        highlighterdshift.forward(60)
        highlighterdshift.right(90)
    highlighterdshift.end_fill()



# The highlighter for the date and time (White):
def time_highlight():
    timehighlighter = turtle.Turtle()
    timehighlighter.hideturtle()
    timehighlighter.penup()
    timehighlighter.goto(-350, 90)
    timehighlighter.pendown()
    timehighlighter.color("white")
    timehighlighter.begin_fill()
  

    for _ in range(2):
        timehighlighter.forward(700)
        timehighlighter.right(90)
        timehighlighter.forward(60)
        timehighlighter.right(90)
    timehighlighter.end_fill()


def upcoming_sched_highlighter():
    upcominghighlighter = turtle.Turtle()
    upcominghighlighter.hideturtle()
    upcominghighlighter.penup()
    upcominghighlighter.goto(-350,-10)
    upcominghighlighter.pendown()
    upcominghighlighter.color("white")
    upcominghighlighter.begin_fill()

    for _ in range(2):
        upcominghighlighter.forward(700)
        upcominghighlighter.right(90)
        upcominghighlighter.forward(60)
        upcominghighlighter.right(90)
    upcominghighlighter.end_fill()



# The primary function for displaying the GUI window, the title of the program, the current working shift, the current date and time, and the current week schedule:
def word_layout(shift,time,weekly_schedule,upcoming_shift):

    screen = turtle.Screen()
    screen.title("Work Shift Tracker")
    screen.bgcolor("black")
    screen.setup(height=850, width=750)

    writer0 = turtle.Turtle()
    writer0.hideturtle()
    writer0.color("white")
    writer0.penup()
    writer0.goto(0, 200)
    writer0.write("Work Shift Tracker\n", align="center", font=("Arial", 30, "bold"))

    writer1 = turtle.Turtle()
    writer1.hideturtle()
    writer1.color("black")
    writer1.penup()
    writer1.goto(0, 95)
    writer1.write(f"{shift}", align="center", font=("Arial", 24, "bold"))

    writer2 = turtle.Turtle()
    writer2.hideturtle()
    writer2.color("black")
    writer2.penup()
    writer2.goto(0, 50)
    writer2.write(f"Time: {time}", align="center", font=("Arial", 24, "bold"))

    writer3 = turtle.Turtle()
    writer3.hideturtle()
    writer3.color("red")
    writer3.penup()
    writer3.goto(0, -370)
    writer3.write(f"{weekly_schedule}", align="center", font=("Arial", 24))

    writer4 = turtle.Turtle()
    writer4.hideturtle()
    writer4.penup()
    writer4.color("black")
    writer4.goto(0, -60)
    writer4.write(f"{upcoming_shift}", align="center", font=("Arial", 24, "bold"))




# The loops for the GUI window, and the exit:
    screen.mainloop()

    screen.exitonclick()


# Calls the main function:
if __name__ == "__main__":
    main()
