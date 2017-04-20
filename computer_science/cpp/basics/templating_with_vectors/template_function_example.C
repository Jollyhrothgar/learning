// Fig. 14.1: fig14_01.cpp
// Using template functions.
#include <iostream>
using std::cout;
using std::endl;

// function template printArray definition
	template< typename T>
void printArray( const T *array, int count )
{
	for ( int i = 0; i < count; i++ )
		cout << array[ i ] << " ";

	cout << endl;
} // end function template printArray

int main()
{
	const int ACOUNT = 5; // size of array a
	const int BCOUNT = 7; // size of array b
	const int CCOUNT = 6; // size of array c

	int a[ ACOUNT ] = { 1, 2, 3, 4, 5 };
	double b[ BCOUNT ] = { 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7 };
	char c[ CCOUNT ] = "HELLO"; // 6th position for null

	cout << "Array a contains:" << endl;

	// call integer function-template specialization
	printArray( a, ACOUNT );

	cout << "Array b contains:" << endl;

	// call double function-template specialization
	printArray( b, BCOUNT );

	cout << "Array c contains:" << endl;

	// call character function-template specialization
	printArray( c, CCOUNT );
	return 0;
} // end main
