// This program gets the user's name, address, and phone number.
// It then captures the inputed data in memory.
// Then it displays the captured input.



//Included the preprocessor:
#include <iostream>
#include <string>
using namespace std;


// Defined the main function:
int main()
{

// Listed the string variables:
    string name, address, phone_number;

// The next three couts asks for the user's name, address, and phone number.
// Each prompt is separated with a newline character for neatness:
    cout << "What is your name?: \n";
    getline(cin, name);
    cout << "\n";

    cout << "What is your address?: \n";
    getline(cin, address);
    cout << "\n";

    cout << "What is your phone number?: \n";
    getline(cin, phone_number);
    cout << "\n";


// There is a header, followed by a dotted line separator, and the captured name, address, and phone number:
    cout << "Here is what was saved" << endl;
    cout << "----------------------" << endl;
    cout << "Name: " << name << endl;
    cout << "Address: " << address << endl;
    cout << "Phone Number:" << phone_number << endl;

// Returns the program:
    return 0;
}