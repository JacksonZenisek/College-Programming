// Jackson Zenisek
// Complete
// This program displays the conversion height of a basketball player who is 75 inches tall to feet and inches form.

// Included the preprocessors:
#include <iostream>
using namespace std;

/* Defined the main function. This function lists a variable for the total inches of the basketball player, and then converts the inches to feet and inches form:
*/
int main(){

// Defined the variables with (int):
    int inches_height, converted_feet, converted_inches;

// The variable with the total inches of the basketball player:
    inches_height = 75;

// The variable that takes the total inches and divides it by 12 (12 inches = 1 foot):
    converted_feet = inches_height / 12;

// Takes the total inches and includes the % operator to get 3 inches:
    converted_inches = inches_height % 12;

// Displays the coverted height of the basketball player from 75 inches to 6 foot 3 inches:
    cout << "A 75 inch tall basketball player is " << converted_feet << " feet " << converted_inches << " tall." << endl;

// Returns the program with no errors:
    return 0;
}