// This program encrypts text into secret code. It adds +10 ASCII to each character in the file to properly encrypt the text.
// Jackson Zenisek
// complete

// Listed the preprocessors:
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Defined the main function:
int main()
{
    
// Listed the string values:
    string inputFile;
    string outputFile;

// Listed the fstream values needed to transfer the text:
    fstream inFile;
    fstream outFile;

// Listed the char value needed to work with each character in the text file:
    char ch;

// Prompts the user to enter the name of the text file needed to be encypted:
    cout << "Enter the file to encrypt: ";
    cin >> inputFile;

// Prompts the user to enter the name of the output encrypted file:
    cout << "Enter the encrypted file name: ";
    cin >> outputFile;

    inFile.open(inputFile, ios::in);

// If the name of the text file does not exist, display an error message:
    if (!inFile)
    {
        cout << "Error opening input file." << endl;
        return 1;
    }

    outFile.open(outputFile, ios::out);

// If the name of the 
    if (!outFile)
    {
        cout << "Error opening output file." << endl;
        return 1;
    }

    ch = inFile.get();

// Encrypts the text by adding +10 ASCII code to each character in the text file:
    while (ch != EOF)
    {
        ch = ch + 10;

        outFile.put(ch);

// If the program fails to write +10 ASCII to the text, the program will display a message:
        if (outFile.fail())
        {
            cout << "Error writing to file." << endl;
            return 1;
        }

        ch = inFile.get();
    }

    if (!inFile.eof())
    {
        cout << "Error reading file." << endl;
    }

// Close both the file to be encrypted and the output encrypted file:
    inFile.close();
    outFile.close();

// If the program completes, the program displays this message:
    cout << "Encryption complete!" << endl;

// Returns the program with no errors:
    return 0;
}