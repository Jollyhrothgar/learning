#include <iostream>
#include <iomanip>
using namespace std;

// Compile, run compiled program from command line:
// :~> g++ main.cpp
// :~> a.out Hello World!

// argc counts the number of arguments, argv stores them all into an array, as characters
int main( int argc, char* argv[] )
{
	cout << "The name used to start the program: " << argv[ 0 ]
		<< "\nArguments are:\n";
	for (int n = 1; n < argc; n++)
		cout << setw( 2 ) << n << ": " << argv[ n ] << '\n';
	return 0;
}
