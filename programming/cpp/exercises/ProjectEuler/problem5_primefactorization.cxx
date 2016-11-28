
// Problem 5
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
// --evenly divisible means 'no remainder'
// See http://mathforum.org/library/drmath/view/62527.html for more info on prime-factorization puzzle.
// The smallest number which shares 1-20 as factors is the product of the prime factors of 1-20.

// We need to find prime factors of the factors, get the biggest, and multiply them together.
// where we could take a number like 8, and factor it as 2^3 (instead of 1,2,4,8), or 10, and
// factor it like 10=2*5 instead of 1,2,5,10, selecting the largest power of a prime factor.

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
	time(&tim);
	cout << "Program started at " << ctime(&tim) << endl;
	cout << "Usage of Factorizer is: ./factorizer.exe <long integer>" << endl;
	vector<long int> my_factors;
	// Test primes
	// calculate_primes(10);
	long int factor_me;
	const char* mychar = argv[1];
	string str_argv_1(mychar);
	stringstream convert(str_argv_1.c_str());
	if( !(convert >> factor_me)) factor_me = 0;

	//factor_me = 150929839212;
	if(isprime(factor_me) == 1)
	{
		cout << factor_me << " is a prime" << endl;
		cout << "Aborting attempt to factor" << endl;
		return 0;
	}
	
	cout << "Factoring " << factor_me << " into all factors and identifying prime factors." << endl;
	factorize(factor_me,my_factors);
	vector<long int> prime_factors;
	long int small = 0;
	long int big = 0;
	long int holder = 0;
	for(vector<long int>::iterator itr = my_factors.begin(); itr!=my_factors.end(); ++itr)
	{
		if((isprime(*itr)) == 1)
		{
			prime_factors.push_back(*itr);
		}
	}
	
	cout << "There were " << prime_factors.size() << " prime factors" << endl;
	sort(prime_factors.begin(),prime_factors.end());
	cout << "Smallest prime factor: " << prime_factors.front() << ", " << "largest prime factor: " << prime_factors.back() << endl;
	cout << "The prime factors are: " << endl;
	for(vector<long int>::iterator itr = prime_factors.begin(); itr!=prime_factors.end(); ++itr)
	{
		cout << *itr << " "; 
	}
	cout << endl;
	cout << "Program finished at " << ctime(&tim) << endl;
	return 0;
}

bool isprime(long int my_int)
{
	bool prime = 1;
	// tests if zero
	if(my_int == 0)
	{
		return 0;
	}
	
	// tests if even
	if(my_int%2 == 0)
	{
		return 0;
	}

	// tests if 1
	if(my_int == 1)
	{
		return 1;
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

void calculate_primes(long int index)
{
	bool test;
	for(long int i = 0; i < index; i++)
	{
		test = 0;
		test = isprime(static_cast<long int>(i));
		if(test == 1)
		{
			cout << i << " is a prime number\n";
		}
	}
}

// factor
void factorize(long int my_int, vector<long int>& factors )
{
	long int term1 = 0;
	long int term2 = 0;
	int counter = 1;
	factors.clear();
	long int max = my_int/2 + 1;

	for(long int i = 1; i < max; i++)
	{
		if(my_int%i == 0)
		{
			term1 = i;
			term2 = my_int/i;
			if(term1 <= term2)
			{
				factors.push_back(term1);
				factors.push_back(term2);		
				cout << term1 << " " << term2 << endl;
				max = term2;
			}
		}
	}
}

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
