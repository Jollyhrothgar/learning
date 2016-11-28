// This program reviews strings, std input/output
#include<iostream>
#include<string>
int main()
{
	//ask person's name
	std::cout << "Please enter your first name: " << std::endl;
	std::string name;	// define name
	std::cin >> name;	// read in
	// Write a greeting
	std::cout << "Hello, " << name << "!" << std::endl;
	return 0;
}
// All variables within these brackets are destroyed when they go out of
// scope -- namely, when the program reaches the end of a block.
