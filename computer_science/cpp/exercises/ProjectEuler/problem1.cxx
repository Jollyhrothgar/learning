// Euler problem 1
// Find the sum of all the multiples of 3 or 5 below 1000
//
#include <iostream>
using namespace std;

int main()
{
	int mult_3 = 0;
	int mult_5 = 0;
	int mult_both = 0;
	for(int i = 0; i < 1000; i++)
	{
		if( (i%3==0) && (i%5!=0) )
		{
			//cout << i << " is a multiple of 3, but not 5\n";
			mult_3+=i;
		}
		if( (i%5==0) && (i%3!=0) )
		{
			//cout << i << " is a multiple of 5, but not 3\n";
			mult_5+=i;
		}
		if( (i%3==0) && (i%5==0) )
		{
			//cout << i << " is a multiple of 5 and 3\n";
			mult_both+=i;
		}
	}
	cout << "The sum of all integers which are multiples of 3 and 5 below 1000 is " 
		 << mult_both + mult_3 + mult_5 << endl;
	return 0;
}
