#include<iostream>
#include<string>
int main()
{
	const std::string hello = "Hello";
	// Accelerated C++ claims that two string-literals cannot be
	// concatinated. However, this code compiles.
	const std::string message = hello + ", world" + "!";
	const std::string exclaim = "!";
	//const std::string message = hello + ", world" + exclaim;
	
	{ 
		const std::string s = "a string";
		std::cout << s << std::endl; 
	}
	
	{
		const std::string s = "another string";
		std::cout << s << std::endl; 
	}
	
	std::cout << message << std::endl;
	return 0;
}
