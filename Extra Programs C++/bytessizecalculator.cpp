// This is a very simple program that counts the number of bytes (size of data) based on what the user inputs to the program.
// The program also counts how many characters long the sentence is.
// I utilized the "sizeof" tool.

// Included the preprocessors:
#include <iostream>
#include <string>
using namespace std;

int main()
{

// Listed the variable that will be used to collect the inputed data:
    string user_sentence;

// The user is prompted to enter a sentence or number:
    cout << "Enter a sentence or a number:";
    getline(cin, user_sentence);

// The program displays the character length of the sentence/number and the number of bytes of memory usage:
    cout << "\n";
    cout << "The text you have entered contains " << user_sentence.length() << " characters and approximately " << user_sentence.length() * sizeof(char) << " bytes of text data." << endl;
    cout << "\n";

// The program also displays the character length:


// Returns the program:
    return 0;
}