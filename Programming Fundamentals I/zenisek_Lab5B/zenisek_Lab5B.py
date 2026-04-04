# Jackson Zenisek
# Complete
"""
This program displays the distance that an object falls in meters per second. 
"Time" is displayed on the left of the chart, and "Distance" is displayed on the right of the chart.
"""
# Imported distance.py to this file:
import distance
# Added the chart header with the spacing element:
print("Time \t Falling Distance")
print("------------------------")
# Defined the main function:
def main():
# Places numbers 1- 10 in a for loop:
    for time_num in range(1, 11):
        
        distance_fallen = distance.falling_distance(time_num)
# Prints the output of the "Time" 1 - 10 seconds, and the fall distance per second in a range of 10 seconds:
        print(f"\n{time_num}\t{distance_fallen:.2f}")
#Calls the main function:
main()