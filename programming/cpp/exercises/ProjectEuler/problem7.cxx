// Problem 7
//
// Find the 10001st prime number
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <time.h>

using namespace std;

int main(int argc, char * argv[])
{
	int t;
	// define a set of numbers, save to a vector.
	stringstream ss(argv[1]);	
	long int set_size;
	ss >> set_size;
		
	vector<long int> sieve_set;
	vector<long int> primes;
	
	for(long int i = 2; i<set_size;i++) sieve_set.push_back(i);
	
	vector<long int>::iterator itr;
	
	bool primes_left = 1;
	primes.push_back(2);
	
	while(primes_left)
	{
		// 1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
		// 2. Initially, let p equal 2, the first prime number.
		// 3. Starting from p, count up in increments of p and mark each of these 
		//	  numbers greater than p itself in the list. These numbers will be 2p, 
		//	  3p, 4p, etc.; note that some of them may have already been marked.
		// 4. Find the first number greater than p in the list that is not marked. 
		//    If there was no such number, stop. Otherwise, let p now equal this 
		//	  number (which is the next prime), and repeat from step 3
		for(itr = sieve_set.begin(); itr < sieve_set.end(); itr++)
		{
			//cout << *itr << endl;
			if((*itr)%((primes.back()))==0) sieve_set.erase(itr);
		}
		primes.push_back(sieve_set.front());
		//cout << sieve_set.front() << endl;
		//if(sieve_set.back() <= primes.back()) break;
		if(primes.size() == 10001) break;
	}
	t = clock();
	cout << primes.size() << " prime numbers found." << endl;
	cout << "The last prime is: " << primes.back() << endl;
	//cout << "The prime you want is " << primes.at(10002) << endl;
	cout << "It took " << t << " clicks, and " << ((float)t/CLOCKS_PER_SEC) << " seconds to run" << endl;
	return 0;
}
