#include<iostream>
using namespace std;

int main()
{
	int TestArray[10][10] = {0};
	int i,j;	
	for(i = 0; i < 10; i++)
	{
		for(j = 0; j < 10; j++)
		{
			TestArray[i][j]++;
		}
	}

	for(i = 0; i < 10; i++)
	{
		for(j = 0; j < 10; j++)
		{
			cout << TestArray[i][j] << "\t";
			if(j == 9)
			{
				cout << endl;
			}
		}
	}
	
	return 0;
}
