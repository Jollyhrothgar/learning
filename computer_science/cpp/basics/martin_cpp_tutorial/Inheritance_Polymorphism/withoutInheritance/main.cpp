// compile with "g++ main.cpp cylinder.cpp cube.cpp"
#include<iostream>
#include "cylinder.h"
#include "cube.h"
using namespace std;
// Information is still hidden, making use of classes easy and straightforward
// Now, we note that all solid objects can be described by common traits - both
// cubes and cylinders, and spheres, etc, all have surface area and volume.
// This idea of many objects having the same traits is called "Polymorphism"
// We can extract the common traits and give a general definition by using
// class inheritance. We can construct a 'parent class' called "bodies"
// and then have specific types of "bodies" inherit traits from "bodies".

int main()
{
	float volume;
	cylinder cylinder(2., 1.);
	cube cube(2.);
	cout << "cylinder volume is: " << cylinder.GetVolume() << endl;
	cout << "cylinder surface area is: " << cylinder.GetSurface() << endl;
	cout << "cube volume is: " << cube.GetVolume() << endl;
	cout << "cube surface area is: " << cube.GetSurface() << endl;
	return 0;
}
