#include <iostream>
#include <cmath>
#include <string>
#include <iomanip>
#include <fstream>
#include <cstdlib>
using namespace std;

int main(){
    
    string employee_name;
    
    double employee_sal, pay_bonus, new_sal, proj_sal;
    
    int employee_years_serv;
    
    char go_again;
    
    ofstream data_transport;
    
do
{
    cout << "Enter the employee name: " << endl;
    getline(cin, employee_name);
    cout << "\n" << endl;
    
    cout << "Enter the annual salary: " << endl;
    cin >> employee_sal;
    cout << "\n" << endl;
    
    cout << "Enter years of service: " << endl;
    cin >> employee_years_serv;
    cout << "\n" << endl;
    
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
        else
        {
            cout << "Invalid input, restart the program and try again.";
            exit(0);
        }
    
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
    
    
    data_transport.open("employeepayrollrecord.txt");
    data_transport << "Employee name: " << employee_name << "\n" << endl;
    data_transport << "Annual Salary: " << employee_sal << "\n" << endl;
    data_transport << "Years of Service: " << employee_years_serv << "\n" << endl;
    
    data_transport << "Bonus Amount: $" << pay_bonus << endl;
    data_transport << "New Salary: $" << new_sal << endl;
    data_transport <<"Projected Salary After 3 Years: $" << proj_sal << "\n" << endl;
    
    cout << "Data has been saved to 'employeepayrollrecord.txt'." << endl;
    
}while (go_again == 'Y' || go_again == 'y');
    
    
    return 0;
}
