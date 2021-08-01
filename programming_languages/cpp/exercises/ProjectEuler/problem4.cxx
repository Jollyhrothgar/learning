// A palindromic number reads the same both ways.
// The largest palindrome made from the product of 
// two 2-digit numbers is 9009 = 91 99.
//
// Find the largest palindrome made from the product 
// of two 3-digit numbers.
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <ctime>

using namespace std;

bool ispalendrome(int);

int main()
{
	int t;
	int product;
	int biggest = 100*100;
	// Generate 3 digit products, check if palendrome
	for(int i = 100; i<=999; i++)
	{
		for(int j = i; j<=999; j++)
		{
			product = i*j;
			if(ispalendrome(product)) 
			{
				if(product > biggest)
				{
					biggest = product;
				}
				//cout << product << endl;
			
			}
		}
	}

	t = clock();	
	cout << "The biggest palendrome product of two three digit numbers is " << biggest << endl;
	cout << "It took " << t << " clicks, and " << ((float)t/CLOCKS_PER_SEC) << " seconds to run" << endl;
	return 0;
}


bool ispalendrome(int myint)
{	
	string numberstring = static_cast<ostringstream*>( &(ostringstream() << myint) )->str();
	int size = numberstring.size();
	int halfway = 0;
	
	string front = "";
	string back = "";

	// even palendromes
	if(size%2 == 0)
	{
		halfway = size/2;
		
		for(int i=0; i < halfway;i++)
		{
			front +=numberstring[i];
		}
		for(int i=(size-1); i>=halfway; i--)
		{
			back += numberstring[i];
		}
		if(front == back)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}

	// odd palendromes
	else
	{
		int halfway = (size-1)/2;
		// halfway is middle of number indexed from zero
		// ie if size is 5, then we will count through as
		// 0, 1, 2, 3, 4; and halfway = 2

		for(int i=0; i < halfway;i++)
		{
			front +=numberstring[i];
		}
		for(int i=(size-1); i>halfway; i--)
		{
			back += numberstring[i];
		}
		if(front == back)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	return 0;
}
