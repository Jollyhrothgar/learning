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
using namespace std;

// brute force method to calculate if a long int is a prime (could be templated, overloaded)
bool isprime(long int);

// test method to calculate all primes between 0 and the integer specified. returns to terminal.
void calculate_primes(long int);

// fill the vector with factors of the first argument
void factorize(long int, vector <long int>&);

int main()
{
	vector<long int> my_factors;
	// Test primes
	// calculate_primes(10);
	
	// Test factorizer
	// factorize(10,my_factors);	
	// cout << my_factors.size() << endl;
	// for(vector<long int>::iterator itr = my_factors.begin(); itr!=my_factors.end(); ++itr)
	// {
	// 	cout << *itr << endl;
	// }

	//factorize(23583,my_factors);
	factorize(600851475143,my_factors);
	//cout << isprime(8462696833) << endl;
	//calculate_primes(600851475143);
	//cout << my_factors.size() << endl;
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
	return 0;
}

bool isprime(long int my_int)
{
	bool prime = 1;
	if(my_int == 0)
	{
		return 0;
	}
	for(long int i = 2; i<my_int; i++)
	{
		if(my_int%i==0)
		{
			return prime = 0;
			break;
		}
	}
	if (prime == 0)
	{
		return 0;
	}
	else return 1;
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
				cout << term1 << ", " << term2 << endl;
				max = term2;
			}
		}
	}
}
