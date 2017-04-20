#include<iostream>
#include "cstring"
#include <vector>
#include <string>

// main.cpp:9:22: warning: deprecated conversion from string constant to ‘char*’
int main()
{
	const char * testString = "What the fuck is going on with Strings?";
	std::cout << std::endl << testString << std::endl;	// Outputs test string correctly
	std::cout << *testString << std::endl;// only outputs first character of testString
	std::string testString2 = "what the fuck is going on with strings, seriously?";
	//const char * myspecialguy = &tesString2;
	std::cout << testString2 << std::endl ;
	// std::cout << *myspecialguy << std::endl; ERROR - type union.
	int i = 0;
	while(testString[i])
	{
		// testString[i] is de-referenced. testString is initialized
		// to first memory address of the string. Its a non-const char
		// array, literally.
		// Two methods with equivalent performance
		// loop condition -> testSting[i]
		// operating on testString[i] with & will output the character
		// currently referenced onward -> &testString[i]
		std::cout << testString[i] << std::endl;
		i++;
		
		/* OR index the pointer to the next sequential address!! */
		//std::cout << *testString << std::endl;
		//testString++; // ++drops in next memory address in sequence.
		//loop condition -> *teststring
	}
	i = 0;
	while(*testString)
	{
		/* This way outputs whole string starting from pointer initialization 	*/
		/* loop condition = testString[i] 										*/
		//std::cout << &testString[i] << std::endl;
		//i++;
		
		/* OR SIMILARLY -> loop = *testString */
		std::cout << testString << std::endl;
		testString++;
	}
	std::cout << std::endl << std::endl;	
	return 0;
}
