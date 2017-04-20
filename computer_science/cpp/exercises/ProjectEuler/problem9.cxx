// A pythagorean triplet is a set of three natural numbers, a  b  c, for which,
//
// a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

// A brute force method:
// 1. Generate pythagorean triplets 
// 		use euclid's formula: any arbitrary pair of m, n integers, m>n
//		a = m^2-n^2, b = 2mn, c = m^2 + n^2 (basically completing the square)
// 2. The test:	in this case, 2m^2+2mn = 1000 is case where we've found the triplet
// 3. Stop looping through m,n pairs when the triplet condition is reached.
#include <iostream>
#include <time.h>
using namespace std;

int main(int argc, char* argv[])
{
	clock_t t; // clock time
	int a,b,c, temp, test;
	// Program start here
	for(int n = 1; n<1001; n++)
	{
		for(int m=(n+1);m<1001; m++)
		{
				test = 2*m*m+2*m*n;
				if(test == 1000)
				{

					a = m*m - n*n;
					b = 2*m*n;
					c = m*m + n*n;
					break;
				}
		}
		if(test == 1000) break;
	}
	// Program end here
	t = clock();
	cout << "The program took " << (float)t/CLOCKS_PER_SEC << " seconds, and " << t << " ticks." << endl;
	cout << "The triplet is: " << a << ", " << b << ", " << c << endl;
	cout << "Test: " << "a^2: " << a*a << " + b^2: " << b*b << " = c^2: " << c*c << endl;
	cout << "Test: " << "a + b + c = " << (a+b+c) << endl;
	cout << "Product abc = " << a*b*c << endl;
	return 0;
}
