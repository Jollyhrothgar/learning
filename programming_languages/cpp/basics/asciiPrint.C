#include <iostream>
#include <vector>

int main(int argc, char* argv[])
{
	std::cout << "This program generates a table of ascii characters" << std::endl;
	char c = 0;
	std::vector<char> vc;

	for(int i = 0; i < 255; i++)
	{
		c = i;
		std::cout << c << std::endl;
	}
	return 0;
}

