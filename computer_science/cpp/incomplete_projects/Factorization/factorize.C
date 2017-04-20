#include <iostream>
using namespace std;

int main()
{
	long int num;
	cout << "What number do you want to factor?\n--> ";
	cin >> num;
	cout << endl;
	for(long int i = 1; i < num; i++)
	{
		if(num%i == 0.0)
		{
			cout << i << endl;
		}
}
	return 0;
}
