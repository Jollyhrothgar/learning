// Note slight change to class-declaration: we say that cube now inherits from
// body's public functions (thus far, there are only public functions.
#ifndef CUBE_H // make sure cube.h gets included only once.
#define CUBE_H // identifies the following as CUBE_H
#include "body.h"

class cube : public body
{
	// Members with same name as inherited functions will override
	// body functions of type virtual.
	protected:
		float length;
	
	public:
		// Overrides funcitons in body
		float GetVolume();
		float GetSurface();
		
		//constructor
		cube(float);

		//destructor
		~cube();
};
#endif // End of CUBE_H
