/* This progam lists 7 employees with their gross pay. This program has two loops: one for reading the data from payroll.bat and
sotring the data in class objects, and another for output data displaying employee numbers with their assigned gross pay.*/
//Jackson Zenisek
//Complete

// Listed the preprocessors:
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

// Defined the class;
class PayRoll
{
// Listed the private variables:
    private:
    
    double hourly_pay_rate;
    
    double hours_worked;
    
    public:
// Listed the set functions:
     void setHourlyPay(double hp)
     {
         hourly_pay_rate = hp;
     }
     
     void setHoursWorked(double hw)
     {
         hours_worked = hw;
     }
     
// Listed the gross pay calculation object:
     double calGrossPay()
     {
         return hourly_pay_rate * hours_worked;
     }
    
};

// Defined the main function:
int main()
{
// Created the array of 7 PayRoll objects:
    const int NUM_EMPLOYEES = 7;
    
    PayRoll workers[NUM_EMPLOYEES];
    
// Opens the file that the program will recieve the hours worked and pay rate data:
    ifstream inputFile("payroll.dat");
    
// Listed the double vairables:
    double hours_worked;
    
    double hourly_pay_rate;
    
// The for loop that calls the set functions from the PayRoll class, and file data:
    for(int count = 0; count < NUM_EMPLOYEES; count++)
    {
        inputFile >> hours_worked >> hourly_pay_rate;
        
        workers[count].setHoursWorked(hours_worked);
        workers[count].setHourlyPay(hourly_pay_rate);
        
    }
    
// The Employee and Gross Pay heading:
    cout << "Employee" << setw(11) << "Gross Pay" << endl;
    cout << "========" << setw(11) << "=========" << endl;
    
// The for loop that displays the 7 employee numbers with the 7 gross pay amounts:
    for(int count = 0; count < NUM_EMPLOYEES; count++)
    {
        cout << setw(4) << (count+1) << ":";
        cout << setw(7) << fixed << setprecision(2);
        cout << "$ " << workers[count].calGrossPay() << endl;
    }
    
// Closes the payroll.bat file:
    inputFile.close();
    
// Returns the program with no errors:
    return 0;
}