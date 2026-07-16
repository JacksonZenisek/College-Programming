// This program collects the total amount of movies that each student has watched and divides them by how many students have been surveys.
// Jackson Zenisek
// Complete

// Listed the preprocessors:
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


// Defined the main function:
int main()
{
   
// Listed the variables:
   int num_of_students;
   int *num_of_movies;
   float movie_average;
   int total_movies = 0;
   
   
 // Prompts the user to enter the amount of students to be surveyed:
   cout << "How many students do you have?: ";
   cin >> num_of_students;
   cout << endl;
   
// Input validation for the amount of students:
   while (num_of_students <= 0)
    {
        cout << "Please enter a positive number of students: ";
        cin >> num_of_students;
    }
   
// The array for the number of students:
   num_of_movies = new int[num_of_students];
   
// The for loop that gets the amount of movies watched per student:
   for (int i = 0; i < num_of_students; i++)
   {
       cout << "Enter the number of movies watched for student " << i + 1 << ": ";
       cin >> *(num_of_movies + i);
      
// Input validation for the amount of movies per student:
       while (*(num_of_movies + i) <= 0)
       {
           cout << "Please enter a positive amount of movies: ";
           cin >> *(num_of_movies + i);
       }
       cout << endl;
   }
   
// Accumulates the total movies of all students:
   for (int i = 0; i < num_of_students; i++)
    {
        total_movies += *(num_of_movies + i);
    }
    
// Calculates the movie average given the amount of movies per student:
    movie_average = (float)total_movies / num_of_students;
   
// Displays the output including the number of movies listed per student, and the average amount of movies:
   cout << "Number of Movies Watched" << endl;
   cout << "------------------------" << endl;
   for (int i = 0; i < num_of_students; i++)
   {
       cout << fixed << setprecision(1);
       cout << *(num_of_movies +i) << endl;
   }
   cout << "----------" << endl;
   cout << "Average " << movie_average;
   
// Closes the number of movies array at the end of the program:
   delete[] num_of_movies;
}