#include <stdio.h>
#include <iostream>
int main()
{
	int index = 0;
	char mychars[20];
	sprintf(mychars,"This is it");
	std::cout << mychars << std::endl;
	sprintf(mychars,"less");;
	std::cout << mychars << std::endl;
	// As you can see from the output, sprintf will overwrite
	// a character array with whatever the input is, provided
	// it fits within the array. So, we can use the same char
	// array to store strings that might have a changing numeric value
	// such as:

	for(index = 0; index < 10; index++)
	{
		sprintf(mychars,"title #%d",index);
		std::cout << mychars << std::endl;
	}
	return 0;
}
