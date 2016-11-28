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
