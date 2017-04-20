// Problem 6
//
// Find the difference between the sum of the squares of the first 100
// natural numbers and the square of the sum
//
// ie: (1+2+3+..+100)^2-(1^2+2^2+3^2+..+100^2)

#include <iostream>
#include <ctime>
#include <time.h>
using namespace std;

int main(int argc, char* argv[])
{
	int t;
	long int sum100=0;
	long int sqr_sum=0;
	long int sum_sqr=0;
	for(long int i = 1; i<=100; i++) sum100+=i;
	for(long int i = 1; i<=100; i++) sqr_sum += i*sum100;
	for(long int i = 1; i<=100; i++) sum_sqr += i*i;

	t = clock();
	cout << sqr_sum-sum_sqr << endl;
	cout << "It took " << t << " clicks, and " << ((float)t/CLOCKS_PER_SEC) << " seconds to run" << endl;

	return 0;
}
