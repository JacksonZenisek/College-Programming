// This program decrypts text by subtracting -10 ASCII code to each character in a text file:
// Jackson Zenisek
// Complete

// Listed the preprocessors:
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Defined the main function:
int main()
{

// Listed the string values:
    string inputName;
    string outputName;
    
// Listed the fstream values needed to decrypt the text:
    ifstream inputFile;
    ofstream outputFile;

// Listed the char value needed to work with each character in the text file:
    char ch;

// Prompts the user to enter the name of the encrypted file:
    cout << "Enter the encrypted file name: ";
    cin >> inputName;

// Prompts the user to enter the decrypted file name:
    cout << "Enter the decrypted file name: ";
    cin >> outputName;

    inputFile.open(inputName);

// If the encrypted file name does not exist, the program will display an error message:
    if (inputFile.fail())
    {
        cout << "Error opening input file." << endl;
        return 1;
    }

    outputFile.open(outputName);

// If the encrypted file name does not exist, the program will display an error message:
    if (outputFile.fail())
    {
        cout << "Error opening output file." << endl;
        inputFile.close();
        return 1;
    }

// The program substracts -10 ASCII code from each character of the encrypted file:
    while (inputFile.get(ch))
    {
        ch = ch - 10;

        outputFile.put(ch);

// If the program fails to decrypt the code, the program will display a message:
        if (outputFile.fail())
        {
            cout << "Error writing to output file." << endl;
            inputFile.close();
            outputFile.close();
            return 1;
        }
    }

// If the program cannot read the file contents, the program will display a message:
    if (!inputFile.eof())
    {
        cout << "Error reading input file." << endl;
    }

// Closes both the encrypted and decrypted files:
    inputFile.close();
    outputFile.close();

// If the program completes, the program will display a message:
    cout << "File decrypted successfully!" << endl;

// Returns the program with no errors:
    return 0;
}