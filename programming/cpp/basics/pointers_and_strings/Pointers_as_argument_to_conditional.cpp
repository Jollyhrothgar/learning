#include <iostream>
int main()
{
	int* pointer_int;
	int myfive = 5;
	char user_resp = 'y';
	pointer_int = &myfive;
	
	// We can use the state of a pointer in conditional statements.
	// The null pointer will evaluate "!pointer" as true, if the pointer
	// is pointing to the NULL address, and will evaluate as "False" if the
	// pointer has an address.
	while((user_resp == 'y')||(user_resp == 'Y'))
	{
		if(pointer_int)
		{
			std::cout << *pointer_int << std::endl;
			pointer_int = 0;
		}
		if(!pointer_int)
		{
			// will segfault if you derefernce the NULL pointer.
			// Error occurs at std::cout, with *pointer_int
			std::cout << pointer_int << std::endl;
			pointer_int = &myfive;
		}
	std::cout << "Continue (y/n)\n" << " -> : ";
	std::cin >> user_resp;
	std::cout << std::endl;
	}
	return 0;
}
