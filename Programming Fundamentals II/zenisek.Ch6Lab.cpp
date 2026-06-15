// This program gets the total amount in sales for each of the 4 divisons (Northeast, Southeast, Northwest, and Southwest)
// Jackson Zenisek
// Complete


// Listed the preprocessors:
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// Listed the constant variable:
const double MIN_SALES = 0.0;

//Listed the global double:
double getSales(string divisionName);

//Listed the void functions:
void findHighest(double northeast, double southeast, double northwest, double southwest);

// Defined the main finction:
int main()
{

//Listed the local doubles:
    double northeast, southeast, northwest, southwest;

    northeast = getSales("Northeast");
    southeast = getSales("Southeast");
    northwest = getSales("Northwest");
    southwest = getSales("Southwest");

    findHighest(northeast, southeast, northwest, southwest);

// Returns the program without any errors:
    return 0;
}

// The getSales function, gets the sales amount for each branch:
double getSales(string divisionName)
{
    double sales;

    cout << "Enter the quarterly sales for the " << divisionName << " division: ";
    cin >> sales;

// The input validation method:
    while (sales < MIN_SALES)
    {
        cout << "Sales figures cannot be negative. Please re-enter." << endl;
        cout << "Enter the quarterly sales for the " << divisionName << " division: ";
        cin >> sales;
    }

// Returns the sales for each branch:
    return sales;
}

void findHighest(double northeast, double southeast, double northwest, double southwest)
{
    
    string highestDivision = "Northeast";
    double highestSales = northeast;

// The switch that determines what branch had the highest sales:
    if (southeast > highestSales)
    {
        highestSales = southeast;
        highestDivision = "Southeast";
    }

    if (northwest > highestSales)
    {
        highestSales = northwest;
        highestDivision = "Northwest";
    }

    if (southwest > highestSales)
    {
        highestSales = southwest;
        highestDivision = "Southwest";
    }

// The out put of the final result of all sales scroes:
    cout << fixed << setprecision(2);
    cout << "\nThe " << highestDivision << " division had the highest sales this quarter." << endl;
    cout << "Their sales were $" << highestSales << endl;
}