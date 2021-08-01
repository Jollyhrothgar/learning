#include<iostream>
using namespace std;
int main()
{
	float floats[100];
	int i = 0;
	float float_index = 0.2;
	
	for(i = 0; i < 100; i++)
	{
		floats[i] = float_index;
		float_index+=0.2;
	}
	
	for(i = 0; i < 100; i++)
	{
		cout << floats[i] << " -> ";
		cout << static_cast<int>(floats[i]) << endl;
	}
	return 0;
}
