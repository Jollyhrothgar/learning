#include<iostream>

// Experiment with what arrays are
int main()
{
	int my_ints[] = {1,2,3,4,5};
	int my_other_ints[5] = {1,2,3,4,5};

	// my_other_ints[] = my_ints[];
	// output memory address of first entry of my_ints
	std::cout << my_ints << std::endl;
	
	//std::cout << my_ints[] << std::endl;
	return 0;
}
