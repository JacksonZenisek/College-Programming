#include <iostream>
using namespace std;

int main()
{
    double hours, rate, final_pay;

    // Gets the hours worked:
    cout << "How many hours did you work?: ";
    cin  >> hours;

    // Gets the hourly rate
    cout << "What is your hourly pay?: ";
    cin  >> rate;

    // Calculates the final pay:
    final_pay = hours * rate;

    // Displays the pay amount:
    cout << "You have earned $" << final_pay << endl;
    
    return 0;
}