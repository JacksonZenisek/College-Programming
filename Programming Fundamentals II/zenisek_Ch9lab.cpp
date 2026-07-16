// This program collects snow fall data anmd then sorts it by the earliest date.
// Jackson Zenisek
// Complete

// Listed the preprocessors:
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

// The maximun amount of entries the program can include:
const int MAX_ENTRIES = 100;

// General structure with the related information together:
struct SnowfallData
{
     string date;
     float inches;
};

//  Protoypes of the program;
void inputSnowfallData(SnowfallData data[], int n);
void sortSnowfallData(SnowfallData data[], int n);
void displaySortedData(SnowfallData data[],int n);


// Defined the main function:
int main()
{
    
// The array for the maximum amount of entries:
    SnowfallData snowData[MAX_ENTRIES];
    int n;

// Prompts the user to enter the number of total snowball entries:
    cout << "Enter the number of snowfall data entries: ";
    cin >> n;

// The input validation method:
    while (n < 1 || n > MAX_ENTRIES)
    {
        cout << "Invalid number. Enter a value between 1 and 100: ";
        cin >> n;
    }


    inputSnowfallData(snowData, n);
    sortSnowfallData(snowData,n);
    displaySortedData(snowData, n);

    return 0;
}

// Collects the date MM/DD and snow inches data:
void inputSnowfallData(SnowfallData data[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << "Enter date (MM/DD): ";
// Captures the dates:
        cin >> data[i].date;

        cout << "Enter snowfall inches: ";
// Captures the snow in inches:
        cin >> data[i].inches;

// Input validation, the amount of snow in inches msut be higher than the int 0:
        while (data[i].inches <= 0)
        {
        cout << "Snowfall inches must be positive. Enter again: ";
        cin >> data[i].inches;
        }
    }
}

// Used bubble sort to list the data:
void sortSnowfallData(SnowfallData data[], int n)
{

    for (int i = 0; i < n - 1; i++)
    {
    for (int j = 0; j < n - i - 1; j++)
        {
        if (data[j].date > data[j + 1].date)
            {
// Saves one record:
            SnowfallData temp = data[j];
// moves econd record:
            data[j] = data[j + 1];
            data[j + 1] = temp;
        }
        }
    }
}



void displaySortedData(SnowfallData data[], int n)
{
    cout << endl;
// The header of the output data:
    cout << "Sorted Snowfall Data at the Taos Ski Area" << endl;
    
    
    cout << "----------------------------------------" << endl;

     cout << fixed << setprecision(1);

    for (int i = 0; i < n; i++)
    {
// The output data of the date in MM/DD and the amount of snow in inches:
        cout << data[i].date << ": " << data[i].inches << " inches" << endl;
    }
}