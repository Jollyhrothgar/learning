#include<iostream>
#include<vector>
#include<string>

struct someInformation
{
	int myInt;
	double myDouble;
	std::string myStrings[3];
	std::vector<std::string> vectStrings;
	bool isTrue;
};

void rootScript()
{
	someInformation info;
	info.myInt = 5;
	info.myDouble = 3.14;
	info.myStrings[0] = "Hello";
	info.myStrings[1] = "There";
	info.myStrings[2] = "Josh";
	info.vectStrings.push_back(" ");
	info.vectStrings.push_back(", ");
	info.vectStrings.push_back("!\n");
	
	std::vector<someInformation> duplicate;
	std::vector<someInformation*> pDuplicate;
	std::vector<someInformation> * pDuplicate2 = NULL; // = new std::vector<someInformation>; // new allocates the vector!

	for (int i = 0; i < 10; i++)
	{
		std::cout << i << " structures stored" << std::endl;
		duplicate.push_back(info);
		pDuplicate.push_back(&info);
		//pDuplicate2->push_back(info);
	}
	pDuplicate2 = &duplicate;

	std::cout << pDuplicate[3]->myStrings[2] << std::endl;
	std::cout << (*pDuplicate[3]).myStrings[1] << std::endl;
	std::cout << "vector of structs size: " << duplicate.size() << std::endl; 
	std::cout << "vector of pointers to structs size: " << pDuplicate.size() << std::endl;
	std::cout << "pointer to vector of structs: " << pDuplicate2->size() << std::endl;

	std::vector<someInformation>::iterator it;
	std::vector<someInformation*>::iterator it_p;
	std::vector<someInformation>::iterator it_p2;

	it_p = pDuplicate.begin();
	it_p2 = pDuplicate2->begin();
	
	std::cout << "Using iterator to access struct elements" << std::endl;
	for (it = duplicate.begin(); it != duplicate.end(); it++)
	{
		std::cout << (*it).myStrings[0] << " ";
	}
	std::cout << std::endl << std::endl;

	std::cout << "Using iterators over a vector filled with pointers to structs" << std::endl;
	for (it_p; it_p != pDuplicate.end(); it_p++)
	{
		std::cout << (*it_p)->myStrings[2];
		std::cout << (*it_p)->vectStrings.at(2);

	}
	std::cout << std::endl;

	std::cout << "Using an iterator with a pointer to a vector filled with structs" << std::endl;
	for (it_p2; it_p2 != pDuplicate2->end(); it_p2++)
	{
		std::cout << (*it_p2).myStrings[0] << (*it_p2).myStrings[1] << std::endl;
	}
	std::cout << std::endl;

}

