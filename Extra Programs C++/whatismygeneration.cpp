// This program tells you what generation you belong to.


// Listed the preprocessors:
#include <iostream>
#include <string>
using namespace std;

// Defined the main function:
int main()
{
    
// Listed the strings that can be displayed based on the user's birth year:
    string GEN_1 = "The Greatest Generation", GEN_2 = "The Silent Generation", GEN_3 = "The Boomer Generation",
           
           GEN_4 = "Generation X", GEN_5 = "The Millennials", GEN_6 = "Generation Z" , GEN_7 = "Generation Alpha", GEN_8 = "Generation Beta";
    
// Listed the birth year variable:
    int input_year;
    
// Listed the go_again char variable:
    char go_again;
    
    
// The "do" section of the do-while loop:
    do
        {
            
// Prompts the user to enter thier birth year:
            cout << "\nEnter your birth year: ";
            cin >> input_year;
            
            
// The if/else if switch, this determines the output generation based on the user's input year:
            if (input_year >= 1901 && input_year <= 1927)
            {
                cout << "\nYou're part of " << GEN_1 << endl;
            }
            else if (input_year >= 1928 && input_year <= 1945)
            
                cout << "\nYou're part of " << GEN_2 << endl;
            
            else if (input_year >= 1946 && input_year <= 1964)
            
                cout << "\nYou're part of " << GEN_3 << endl;
                
            else if (input_year >= 1965 && input_year <= 1980)
            
                cout << "\nYou're part of " << GEN_4 << endl;
            
            else if (input_year >= 1981 && input_year <= 1996)
            
                cout << "\nYou're part of " << GEN_5 << endl;
                
            else if (input_year >= 1997 && input_year <= 2012)
            
                cout << "\nYou're part of " << GEN_6 << endl;
                
            else if (input_year >= 2013 && input_year <= 2025)
            
                cout << "\nYou're part of " << GEN_7 << endl;
                
            else if (input_year == 2026)
                
                cout << "\nYou're part of " << GEN_8 << endl;
               
// The input validation method: 
            else
            
                cout << "Not a valid year, please try again.";
                
// The "go again" prompt:
        cout << "\nWould you like to enter another year? (y = yes, n = no): ";
        cin >> go_again; 
        }
   
// The "while" section of the do-while loop:
   while (go_again == 'Y' || go_again == 'y');
   
// Returns the program with no errors:
    return 0;
}