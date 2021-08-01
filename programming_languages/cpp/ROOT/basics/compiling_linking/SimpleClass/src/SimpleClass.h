#include <iostream>

class SimpleClass
{
	public:
		SimpleClass();
		~SimpleClass();

		int an_obvious_variable;
		int SetSecret(int);
	private:
		int a_secret_variable;
};
