// Note that since body can't be instantiated, is not included in "main". We never care about
// making a body class, just using classes that inherit from the parent class. So, we just
// include the headers that we want to use. Any class with additional dependancies should
// have those dependancies declared in the class header file. Naturally, we must protect
// all headers (aka dependances) so that they aren't over-included. As an experiment - try
// to compile this program where body.h is only included here, in main, removing it from the
// other class headers.
#include "functions.h"
#include<iostream>
#include "cube.h"
#include "cylinder.h"
using namespace std;
// Example of inheritance. Different solids will inherit from body, an abstract parent class
// which cannot be instantiated. Each unique solid has a surface area and volume, so these
// are defined in the abstract parent class as a virtual type. When we create specific body
// subclasses, we make member functions of the same name which override the functions, or data types
// declared in the parent class, body.
int main()
{
	body *p1;
	body *p2;


	p1 = new cube(2.5);
	p2 = new cylinder(2.,5.);

	cout << "Volume of cube: " << p1->GetVolume() << endl;
	cout << "Surface of cube: " << p1->GetSurface() << endl;
	
	cout << "Volume of cylinder: " << p2->GetVolume() << endl;
	cout << "Surface of cylinder: " << p2->GetSurface() << endl;

	// Note that an array of pointers is extremely powerful
	// in the declaration of the array - see that we can set a pointer
	// to anything we want - whether that be a class, or the "NULL" pointer
	body * bodylist[10];
	bodylist[0] = new cube(1.25);
	bodylist[1] = new cube(1.);
	bodylist[2] = new cylinder(1.,1.);
	bodylist[3] = new cylinder(0.5,2.);
	bodylist[4] = new cube(1.25);
	bodylist[5] = new cylinder(1.,2.);
	bodylist[6] = new cylinder(1.,0.5);
	bodylist[7] = new cylinder(3.,2.);	
	bodylist[8] = 0;	// Odd assignment - pointers store memory addresses
						// a type or class - but we can assign memory addresses
						// manually. I guess...
	
	cout << "The total volume is: " << totalVolume(bodylist) << endl;
	
	return 0;
}
