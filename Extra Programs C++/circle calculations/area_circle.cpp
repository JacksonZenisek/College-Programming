// This program calculates a circles area based on radius input from the user.
// This time I focused on utilizing <cmath> and "pow" for exponents.

// Included the preprocessors:
#include <iostream>
#include <cmath>
using namespace std;

// Defined the main function:
int main(){


// Listed the variables under double since they are floats:
    double entered_radius, area_circle;


// Prompts the user to enter the radius:
    cout << "Enter the radius of the circle: ";
    cin >> entered_radius;

// Program performs the calculation (pi * radius to the power of 2):
    area_circle = 3.14159 * pow(entered_radius, 2);

// Program displays the area of the circle:
    cout << "The area of the circle is: " << area_circle << endl;

// Program returns with no errors:
    return 0;
}