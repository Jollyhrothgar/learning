#include <iostream>
using namespace std;

class cube
{
	protected:
		float length;
	
	public:
		float GetVolume();
		float GetSurface();
	
		cube(float);
};
