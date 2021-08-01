#include<iostream>
#include "cylinder.C" // This is very poor coding etiquette. A class
					  // file should always be linked to the final
					  // executable with a makefile.


using namespace std;


// example of information hiding. We have formed a class for a solid
// object, and, can ask the class to calculate this object's properties
// for us, without worring about the particulars. Normally, one considers
// "who is the author of main", and one does not write all the class-files.

// compile with "g++ main.C -o example.exe
// run example ./example.exe

int main()
{
	float volume;
	cylinder c(2., 1.);
	volume = c.GetVolume();
	cout << "volume is: " << volume << endl;
	return 0;
}
