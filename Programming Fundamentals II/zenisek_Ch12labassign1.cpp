/* This program recieves a sentence input from the user without any spaces and converts the sentence with proper spaces in between each word, 
and starts the first word of the sentence with a capital letter.
*/
//Jackson Zenisek
// Complete

// Listed the preprocessors:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

// Defined the main function:
int main()
{

// Defined the string values:
    string input_sentence;
    string result_sentence;
    
// Prompts the user to enter the sentence:
    cout << "Enter a sentence with no spaces: ";
    getline(cin, input_sentence);
    
// If the user does not input anything, the program will not display anything:
    if (!input_sentence.empty())
    {
        result_sentence += input_sentence[0];
        
// The loop for the second character to begin and the 
        for (size_t i = 1; i < input_sentence.length(); i++)
        {
// If the first character of the sentence is uppercase, then the program returns the string with spaces and the first character as an uppercase:
            if (isupper(static_cast<unsigned char>(input_sentence[i])))
            {
                    result_sentence += ' ';
                result_sentence += static_cast<char>(tolower(static_cast<unsigned char>(input_sentence[i])));
            }
// If the first character in the sentence is lowercase, the rogram displays the input sentence as it originally was inputed by the user:
            else
            {
                result_sentence += input_sentence[i];
            }
        }
    }

// The program returns the new version of the sentence:
    cout << "New sentence: " << result_sentence << endl;
    
// Returns the program with no errors:
    return 0;
}