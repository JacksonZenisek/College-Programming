// Jackson Zenisek
// Complete
// This program calculates the time it take for a sound wave to travel throught a specific medium.


// Included the preprocessors:
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;


// Defined the main function:
int main()
{
    
// Listed the strings, specifically for the main menu:
    string air_display = "1. Air",
           water_display = "2. Water",
           steel_display = "3. Steel";
           
// Listed the doubles for the feet entry prompt, and the time outputs:
    double feet_entered,
           air_distance,
           water_distance,
           steel_distance;
           
// Listed the integers, specificallty for the main menu input prompt:
    int air_option = 1,
        water_option = 2,
        steel_option = 3,
        user_menu_selector;
    
// A brief discription of that the program does:
    cout << "This program will tell you how long it takes a sound wave \n to travel a specific distance through a particular medium.\n" << endl;
    
// Prompts the user to enter an option: Air, Water, or Steel:
    cout << "Select a substance for the sound to travel through:" << endl;
    
    cout << setw(11) << air_display << endl;
    cout << setw(13) << water_display << endl;
    cout << setw(13) << steel_display << endl;
    cin >> user_menu_selector;
    cout << "\n";
    
    
// The main conditions:
// If the user selects '1', the user will be taken to the air condition:
    if (user_menu_selector == 1)
    {
        
        cout << "Enter the number of feet the sound wave will travel: ";
        cin >> feet_entered;
        air_distance = feet_entered / 1100 ;
        cout << "The sound wave will travel " << fixed << setprecision(0) << feet_entered <<  " feet through air in " << fixed << setprecision(4) << air_distance << " seconds.";
        
    }
    
// If the user selects '2', the user will be taken to the water condition:
    else if (user_menu_selector == 2)
    {
        cout << "Enter the number of feet the sound wave will travel: ";
        cin >> feet_entered;
        water_distance = feet_entered / 4900;
        cout << "The sound wave will travel " << fixed << setprecision(0) << feet_entered <<  " feet through water in " << fixed << setprecision(4) << water_distance << " seconds.";
    }
    
// If the user selects '3', the user will be taken to the steel condition:
    else if (user_menu_selector == 3)
    {
        cout << "Enter the number of feet the sound wave will travel: ";
        cin >> feet_entered;
        steel_distance = feet_entered / 16400;
        cout << "The sound wave will travel " << fixed << setprecision(0) << feet_entered <<  " feet through steel in " << fixed << setprecision(4) << steel_distance << " seconds.";
    }
    
// The input validation:
// If the user inputs anything other than 1, 2, or 3, then the user will be prompted with this message:
    else
    {
        cout << "Invalid option, restart the program and try again.";
    }

// Returns the program with no errors:
    return 0;
}