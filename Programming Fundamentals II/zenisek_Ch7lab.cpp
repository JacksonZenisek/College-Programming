// This program takes the given population entered by the user, and calculates the birth rate and death rate based on the provided population by the user.
// Complete
// Jackson Zenisek

// Listed the preprocessors
#include <iostream>
#include <iomanip>
using namespace std;

// Defined the class Population:
class Population 
{
    
// Listed the private variables:
    private:
        int population;
        int births;
        int deaths;
    
// Listed the public sets;
    public:
        Population(int p, int b, int d)
        {
            setPopulation(p);
            setBirths(b);
            setDeaths(d);
        }

// Listed the void condition functions of the populations, births, and deaths:
void setPopulation(int p)
{
    if (p < 2)
        population  = 2;
    else
        population = p;
}

void setBirths(int b)
{
    if(b < 0)
        births = 0;
    else
        births = b;
}

void setDeaths(int d)
{
    if (d < 0)
        deaths = 0;
    else
        deaths = d;
}

// Returns the population value:
int getPopulation()
{
    
    return population;
}

// Returns the births value:
double getBirths()
{
    return births;
}

// Returns the deaths value:
double getDeaths()
{
    return deaths;
}

// Listed the calculations for briths rate and death rate:
double getBirthRate()
{
    return static_cast<double>(births) / population;
}

double getDeathRate()
{
    return static_cast<double>(deaths) / population;
}

};

// Defined the main function:
int main()
{
    
// Listed the objects:
    int population;
    int births;
    int deaths;
    
// Prompts the user to enter the population of the area, the yearly births, and yearly deaths:
    cout << "Enter total population: ";
    cin >> population;
    
    cout << "Enter annual number of births: ";
    cin >> births;
    
    cout << "Enter annual number of deaths: ";
    cin >> deaths;
    
    Population area(population, births, deaths);
    
// Displays the entered population, the output birth rate to the third decimal place, and the death rate to the third decimal place:
    cout << fixed << setprecision(3);
    cout << "\nPopulation Statistics\n\n";
    cout << "Population: " << area.getPopulation() << endl;
    cout << "Birth Rate: " << area.getBirthRate() << endl;
    cout << "Death Rate: " << area.getDeathRate() << endl;
    
// Returns the program with no errors:
    return 0;
}