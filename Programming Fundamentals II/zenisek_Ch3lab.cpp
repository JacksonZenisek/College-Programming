// Jackson Zenisek
// Complete
// This program calculates the property tax, and assessed tax based on the input property tax.

// Included the preprocessors:
#include <iostream>
#include <iomanip>
using namespace std;


// Defined the main function:
int main(){

// Listed the vairables as doubles since they are floats:
    double 
        property_value, 
        assessed_value, 
        property_tax,
        final_property_tax_value
    ;

// Prompts the user to enter the property value:
    cout << "Enter the actual property value: $";
    cin >> property_value;

// Prompts the user to enter the amount taxed per $100 of the assessed value:
    cout << "Enter the amount of tax per $100 of assessed value: $";
    cin >> property_tax;
    cout << "\n";

// Calculates the assessed value which is 60% of the property value:
    assessed_value = (property_value / 5 ) * 3;
    
// Calculates the total property tax based on the amount taxed per $100 of the assessed value:
    final_property_tax_value = (assessed_value / 100) * property_tax;

// Displays the property value, assessed value, and property tax with the floats aligned by their decimals:
    cout << fixed << showpoint << setprecision(2);
    cout << left << setw(17) << "Property Value:" << "$" << right << setw(11) << property_value << endl;
    cout << left << setw(17) << "Assessed Value:" << "$" << right << setw(11) << assessed_value << endl;
    cout << left << setw(17) << "Property Tax:" << "$" << right << setw(11) << final_property_tax_value << endl;

// Returns the program with no errors:
    return 0;
}