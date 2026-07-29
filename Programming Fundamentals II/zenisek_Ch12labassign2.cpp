// This program accepts an input string from the user, and converts the string to 3 different formats: all uppercase, all lowercase, and a flipped character version.
// Jackson Zenisek
//Complete

// Defined the preprocessors:
#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;

const int SIZE = 500;

// Listed the functions used in this program:
        void upper(char str[]);
        void lower(char str[]);
        void flip(char str[]);
        
// The uppercase function:
void upper(char str[])
{
//  uppercase keeps looping the chars until the program reaches the null char:
    for (int i = 0; str[i] != '\0'; i++)
    {
//Replaces the current character to uppercase:
        str[i] = static_cast<char>(
            toupper(static_cast<unsigned char>(str[i]))
        );
    }
}



// The lowercase function:
void lower(char str[])
{
// lowercase keeps looping the chars until the program reaches the null char:
    for (int i = 0; str[i] != '\0'; i++)
    {
 //Replaces the current character to lowercase:
             str[i] = static_cast<char>(
            tolower(static_cast<unsigned char>(str[i]))
        );
    }
}

//The flip function:
void flip(char str[])
{
// flip keeps looping the chars until the program reaches the null char:
        for (int i = 0; str[i] != '\0'; i++)
    {
// Flips the uppercase character to a lowercase character:
        if (isupper(static_cast<unsigned char>(str[i])))
        {
            str[i] = static_cast<char>(
                tolower(static_cast<unsigned char>(str[i]))
            );
        }
// Flips the lowercase character to a uppercase character:
        else if (islower(static_cast<unsigned char>(str[i])))
        {
                    str[i] = static_cast<char>(
                toupper(static_cast<unsigned char>(str[i]))
            );
        }
    }
}

// Defined the main function:
int main()
{
    
// The char variables for each 
    char original[SIZE];
    char uppercase[SIZE];
    char lowercase[SIZE];
    char flipped[SIZE];
    
// Prompts the user to input a string:
    cout << "Enter the string: ";
    cin.getline(original, SIZE);

    strcpy(uppercase, original);
    strcpy(lowercase, original);
    strcpy(flipped, original);

// Calls the void functions to the main function:
    upper(uppercase);
    lower(lowercase);
    flip(flipped);

// Displays the output of the original, lowercase, uppercase, and flipped versions of the string:
    cout << "\nOriginal string: " << original << endl;
    cout << "Uppercase string: " << uppercase << endl;
    cout << "Lowercase string: " << lowercase << endl;
    cout << "Flipped case string: " << flipped << endl;

// Returns the program with no errors:
    return 0;
}