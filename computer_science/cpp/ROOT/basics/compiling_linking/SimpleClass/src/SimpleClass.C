#include "SimpleClass.h"

SimpleClass::SimpleClass()
{
	std::cout << "Hello" << std::endl;
}

SimpleClass::~SimpleClass()
{

}

int SimpleClass::SetSecret(int thevalue)
{
	a_secret_variable = thevalue;
	return a_secret_variable;
}
