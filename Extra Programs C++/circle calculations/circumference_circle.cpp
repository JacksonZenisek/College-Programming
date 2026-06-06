// This program calculates a circles circumference based on radius input from the user.

// Included the preprocessors:
#include <iostream>
using namespace std;

// Defined the main function:
int main(){

// Listed the variables under double since they are floats:
    double entered_radius, circle_circumference;

// Prompts the user to enter the radius:
    cout << "Enter the radius of the circle: ";
    cin >> entered_radius;

// Program performs the calculation (2 * pi) * radius:
    circle_circumference = (2 * 3.14159) * entered_radius ;
    
// Program displays the circumference of the circle:
    cout << "The circle has a radius of: " << circle_circumference << endl;


// Program returns with no errors:
    return 0;

}