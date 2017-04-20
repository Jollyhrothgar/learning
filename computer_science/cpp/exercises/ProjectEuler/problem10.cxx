// Problem 10
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.
//
#include <iostream>
using namespace std;

// Use sieve of eratosthenes
int main(int argc, char * argv[]);
{
	if(argv[0])
	{
		int limit = argv[0];
		double lowest_prime = //loopcutoff wp;
		double highest_prime;
		vector<bool> set(limit+1); // this way the container# is the test number
								   // and quantitiy is if the number is prime
		fill(set.begin(),set.end(),true); // start with all primes, then cross out
										  // non-primes
		while(highest prime > lowest_prime)
		{
			for(long int i = 2; i < limit+1; i++) // Cross out numbers
			{
			
			}
		}
	}
	else
	{
		cout << "Please give an upper limit in the prime search (integer only)\n";
		return 0;
	}
}
