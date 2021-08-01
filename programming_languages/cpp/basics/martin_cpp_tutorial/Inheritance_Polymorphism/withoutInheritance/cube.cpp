// for headers not in the standard library, one must tell the compiler
// where to look. For local headers, "<header>" is sufficinet
#include "cube.h"

float cube::GetVolume()
{
	return length*length*length;
}

float cube::GetSurface()
{
	return 6.0*length*length;
}

cube::cube(float l)
{
	length = l;
}
