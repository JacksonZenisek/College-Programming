// This program gets the employee's name, annual salary, and the years of service for the company.
/* The program then displays the output information based on these rules: 

    Less than 5 years of service = 5% bonus;
    5 -10 years of service = 10% bonus;
    More than 10 years of service = 15% bonus;
*/
// The program then displays the employee's name, annual salary, years of service, bonus amount, new salary, and project salary for the next 3 years.

// Listed the preprocessors:
#include <iostream>
#include <cmath>
#include <string>
#include <iomanip>
#include <fstream>
#include <cstdlib>
using namespace std;

// Defined the main function:
int main(){

// Listed the string variable:
    string employee_name;

// Listed the float variable:
    double employee_sal, pay_bonus, new_sal, proj_sal;

// Listed the years of service variable:
    int employee_years_serv;

// Listed the go again loop variable:
    char go_again;

// Listed the file data variable, creates and writes to the file:
    ofstream data_transport;

// The do-while loop:
do
{

// Prompts the user to enter thier name, annual salary, and years of service:
    cout << "Enter the employee name: " << endl;
    getline(cin, employee_name);
    cout << "\n" << endl;
    
    cout << "Enter the annual salary: " << endl;
    cin >> employee_sal;
    cout << "\n" << endl;
    
    cout << "Enter years of service: " << endl;
    cin >> employee_years_serv;
    cout << "\n" << endl;

// The if/else if switch for the calculations of the new pay based on the input annual salary and years of service:
        if (employee_years_serv >= 0 && employee_years_serv <= 5)
        {
            pay_bonus = employee_sal * 0.05;
            
            new_sal = pay_bonus + employee_sal;
            
            proj_sal = employee_sal * pow((1+ 0.05), 3);
            
        }
        else if (employee_years_serv >=5 && employee_years_serv <= 10)
        {
            pay_bonus = employee_sal * 0.1;
            
            new_sal = pay_bonus + employee_sal;
            
            proj_sal = employee_sal * pow((1 + 0.1), 3);
            
        }
        else if (employee_years_serv > 10)
        {
            pay_bonus = employee_sal * 0.15;
            
            new_sal = pay_bonus + employee_sal;
            
            proj_sal = employee_sal * pow((1 + 0.15), 3);
            
        }
// The input validation method, exits the program:
        else
        {
            cout << "Invalid input, restart the program and try again.";
            exit(0);
        }

// The outputs based on the given input information from the user:
    cout << "Employee Bonus Report" << endl;
    cout << "---------------------\n" << endl;
    
    cout << "Employee Name: " << employee_name << endl;
    cout << "Years of Service: " << employee_years_serv << "\n" << endl;
    
    cout << left << fixed << setprecision(2);
    cout << "Current Salary: $" << employee_sal << endl;
    cout << setw(13) << "Bonus Amount: $" << pay_bonus << endl;
    cout << setw(13) << "New Salary: $" << new_sal << endl;
    cout << setw(13) << "Projected Salary After 3 Years: $" << proj_sal << "\n" << endl;
    
    cout << "Would you like to calculate another bonus? (y/n): ";
    cin >>  go_again;
    cin.ignore(1000, '\n');
    
// The transported information from this C++ program to the 'employeepayrollrecord.txt' file:
    data_transport.open("employeepayrollrecord.txt");
    data_transport << "Employee name: " << employee_name << "\n" << endl;
    data_transport << "Annual Salary: " << employee_sal << "\n" << endl;
    data_transport << "Years of Service: " << employee_years_serv << "\n" << endl;
    
    data_transport << "Bonus Amount: $" << pay_bonus << endl;
    data_transport << "New Salary: $" << new_sal << endl;
    data_transport <<"Projected Salary After 3 Years: $" << proj_sal << "\n" << endl;
    
    cout << "Data has been saved to 'employeepayrollrecord.txt'." << endl;

// The condition rules if the user wants to enter another bonus calculation:
}while (go_again == 'Y' || go_again == 'y');
    
// Returns the program with no errors:
    return 0;
}
