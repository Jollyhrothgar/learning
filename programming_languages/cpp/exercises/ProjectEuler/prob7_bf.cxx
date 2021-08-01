// Problem 3
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?
//

// Solution
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <time.h>

using namespace std;

// brute force method to calculate if a long int is a prime (could be templated, overloaded)
bool isprime(long int);

// test method to calculate all primes between 0 and the integer specified. returns to terminal.
void calculate_primes(long int);

// fill the vector with factors of the first argument
void factorize(long int, vector <long int>&);

// argc is number of arguments (space separated) given
// argv is an array which holds the name of the exe, and all args in order.

time_t tim;

int main(int argc, char * argv[])
{
	int t;
	long int factor_me;
	const char* mychar = argv[1];
	string str_argv_1(mychar);
	stringstream convert(str_argv_1.c_str());
	if( !(convert >> factor_me)) factor_me = 0;
	calculate_primes(factor_me);
	
	t = clock();
	cout << "It took " << t << " clicks, and " << ((float)t/CLOCKS_PER_SEC) << " seconds to run" << endl;
}

bool isprime(long int my_int)
{
	bool prime = 1;
	// tests if zero
	if(my_int == 0)
	{
		return 0;
	}
	
	if(my_int == 2)
	{
		return 1;
	}
	// tests if even
	if(my_int%2 == 0)
	{
		return 0;
	}

	// tests if 1
	if(my_int == 1)
	{
		return 0;
	}

	for(long int i = 2; i<my_int; i++)
	{
		if(my_int%i==0)
		{
			prime = 0;
			break;
		}
	}
	if (prime == 1)
	{
		return 1;
	}
	else return 0;
}

void calculate_primes(long int this_many)
{
	int n = 0;
	long int prime = 0;
	while(n <= this_many)
	{
		for(long int i = prime; ; i++)
		{	
			if(isprime(i))
			{
				//cout << i << " is a prime number\n";
				n++;
				prime=i+2;
				if(n==this_many) cout << i << endl;
				break;
			}
		}
	}
}
