// Problem 5
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
// --evenly divisible means 'no remainder'


#include<iostream>
#include<ctime>
#include<time.h>
using namespace std;

int main(int argc, char* argv[])
{
	int t;
	bool success = 0;
	long int i = 18;
	while(success == 0)
	{
		i+=2;
		success = 1;
		//cout << "Testing " << i << endl;
		for(long int j = 2; j<=20; j++)
		{
			if(i%j!=0) 
			{
				success = 0;
				break;
			}
		}
	}

	t = clock();	
	cout << "There smallest number which is evenly divisible by 1-20 is: " << i << endl;
	cout << "It took " << t << " clicks, and " << ((float)t/CLOCKS_PER_SEC) << " seconds to run" << endl;
	return 0;
}
