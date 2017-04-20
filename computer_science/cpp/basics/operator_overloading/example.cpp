#include <iostream>
#include "Vector.h"
using namespace std;

int main()
{
	cout << "\nThis program demonstrates the overloading of the \"+\" operator.\n";
	CVector vect1(1.2,3.8);
	CVector vect2(9.9,-3.2);
	CVector vect3;
	
	cout << "Vector 1 is: (" << vect1.x <<  ", " << vect1.y << ").\n";
	cout << "Vector 2 is: (" << vect2.x <<  ", " << vect2.y << ").\n";
	
	cout << "We can add the vectors using our overloaded \"+\"\n";
	
	vect3 = vect1 + vect2;
	
	cout << "Vector 3 is v1 + v2: (" << vect3.x <<  ", " << vect3.y << ").\n\n";

	return 0;
}	
