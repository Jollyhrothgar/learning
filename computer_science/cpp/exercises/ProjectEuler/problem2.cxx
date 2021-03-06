// Each new term in the Fibonacci sequence is generated by adding 
// the previous two terms. By starting with 1 and 2, the first 10 
// terms will be:
// 
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values 
// do not exceed four million, find the sum of the even-valued terms.

#include <iostream>
using namespace std;

int main()
{
	long int fib_prev = 1;
	long int fib_next = 2;
	long int fib_hold = 0;
	long int max = 4000000;
	int terms = 1;
	long int evenfib = 0;
	cout << "First 10 fib: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n";
	while(fib_prev < max)
	//while(terms <= 10 )
	{
		//cout << fib_prev << ", ";
		fib_hold = fib_next;
		if(fib_next%2 == 0)
		{
			evenfib+=fib_next;
		}
		fib_next = fib_prev + fib_next;
		fib_prev = fib_hold;
		terms++;
	}
	cout << "There were "  << terms << " terms" << " in the fibonacci series"
		 << " whose values were less than " << max << endl;
	cout << "The answer is: " << evenfib << endl;
	return 0;
}
