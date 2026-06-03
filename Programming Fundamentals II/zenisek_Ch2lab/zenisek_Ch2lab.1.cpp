// Jackson Zenisek
// Complete
// This program displays how much each flash drive should sell if the electronics company wants to reach a goal of 35 percent profit.


// Included the preprocessors:
#include <iostream>
using namespace std;

/* Defined the main function. This function lists a variable for both the starting price and the profit goal price of each flash drive.
   The function also displays what the cost of each flash drive should be if the electronics company wants a 35 percent profit.
*/
int main()
{

//Declared the variables with (double):
    double starting_flashdrive_price, profit, selling_price;

// The default price of the flash drives:
    starting_flashdrive_price = 8.00;

// 35% of the default price:
    profit = starting_flashdrive_price * 0.35;

// The profit price (default price + 35% of the default price = final selling price):
    selling_price = starting_flashdrive_price + profit;

// Displays the output:
    cout << "To have a 35% profit, the flash drive should sell for $" << selling_price << endl;


// Returns the program with no errors:
    return 0;
}