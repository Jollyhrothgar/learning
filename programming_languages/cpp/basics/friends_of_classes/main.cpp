#include <iostream>
#include "Secret_X.C"
using namespace std;

// Unquote to see what happens when a non-friend trys to access
// private data of a class.
// int cantread(Secret_X);

int main()
{
	Secret_X Big_Secret;
	Big_Secret.init_X(5);
	
	cout << "The secret x is " << read_x(Big_Secret) << endl;
	//cout << "The secret x is " << cantread(Big_Secret) << endl;
	return 0;
}

/*
int cantread(Secret_X temp2)
{
	return temp2.x;
}
*/
