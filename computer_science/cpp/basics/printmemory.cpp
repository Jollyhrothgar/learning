#include <iostream>
#include <string>
using namespace std;

int main()
{

	string startingString = "start";
	int    startingInt    = 2;
	double startingDouble = 3.0;

	string* s = &startingString;
	int* i    = &startingInt;
	double* d = &startingDouble;
	char ans = 'Y';
	while(ans != 'N')
	{
		cout << "The int    address in Memory is: " << *s << endl;
		cout << "The double address in memory is: " << *i << endl;
		cout << "the string address in memory is: " << *d << endl;

		cout << "Want to see more? (Y/N)\n-> ";
		cin >> ans;
		ans = toupper(ans);

		cout << endl;
		s++;
		i++;
		d++;
	}
	return 0;
}
