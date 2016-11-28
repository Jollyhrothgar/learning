#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

// TODO
// input file streams, output file streams
// write a function
// use a pointer
// define a class, class header, use class
// review class writing
// call math function, output two-column data

int main()
{
	ostream teststr("data.txt");
	teststr.open();
	teststr << "Hello, World\n";
	teststr.close();
	return 0;
}
