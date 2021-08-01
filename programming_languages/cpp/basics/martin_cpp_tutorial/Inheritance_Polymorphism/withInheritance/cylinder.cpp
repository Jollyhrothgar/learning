#include "cylinder.h"

//using the header file, we can now define the attributes of the
//cylinder object

//Constructor definition - note that constructor, as a member function
//has access to private data, such as r and h.
cylinder::cylinder(float r, float h)
{
	radius = r;
	height = h;
}

// Define other memberfunctions
// 1. <return type> <class scope>::<function name>
float cylinder::GetSurface()
{
	return (2.0*PI*height*radius + 2.0*radius*radius*PI);
}
float cylinder::GetVolume()
{
	return (PI*radius*radius*height);
}

