#include "functions.h"

float totalVolume(body * bptr[])
{
	int i = 0;
	float volume = 0;
	body * b = bptr[i++];

	// The concept of a zero terminated array is used here.
	// in this case, the while loop will iterate until reaching
	// zero (which is like a 'false' which will terminate the
	// iteration, break out of the loop give us the return
	// return statement. A pointer to NULL (also zero) when
	// passed to a while statement will evaluate false.
	// while statements loop only while contition is true.

	while(b)// passing pointer value, no dereferencing.
	{
		volume += b->GetVolume();
		b = bptr[i++];
	}
	return volume;
}
