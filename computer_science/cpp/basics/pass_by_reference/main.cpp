#include <iostream>
#include "swap.h"
using namespace std;

// referencing takes the address of a variable. When we pass by reference
// the function will take normal variables as arguements, but instead of
// copying their value into the function, operating on those values, and then
// returning a single data type, the declaration of the function
// instructs the function to instead take the address of the variables, and
// operations in the function will change the actual value of the outside
// variables. This can be used with "void" function type to generate
// multiple return values.
int main()
{
	int x = 1;
	int y = 2;

	cout << "X is " << x << " and Y is " << y << endl;
	// If x and y were not passed by reference,
	// the function swap would copy the value of x and y
	// and swap them, but this would only affect variables
	// in the scope of swap. Passing by reference lets swap operate
	// on variables inside main directly.
	swap(x,y);
	cout << "X is " << x << " and Y is " << y << endl;

	return 0;
}
