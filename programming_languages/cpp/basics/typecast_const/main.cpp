#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	const int num1 = 15;		// this is a constant integer that cannot be changed.
	int num2 = 10;
	printf("num2 = %i\n",num2);
	cout << "num1 = " << num1 << endl;
	cout << "num1 + 1 = " << num1 + 1 << endl;	// no problem here, we're not modifying cint.
	/*num1 = num1 + 1; ERROR */
	const int * Cpint2 = &num2;	// (C = const) create a pointer which points to and can reference
								// num2, but cannot be used to modify num2
	int * Mpint2 = &num2;		// This pointer CAN modify num2, since neither num2 or
								// Mpint2 are of type const int. (M = mutable)
								// defining a const <type> is known as typecasting.
	cout << "*Mpint2 = " << *Mpint2 << endl;
	cout << "*Cpint2 = " << *Cpint2 << endl;
	
	*Mpint2 = *Mpint2 + 1;
	cout << "*Mpint2 + 1 modifys num2. num2 = " << num2 << endl;
	cout << *Cpint2 << endl;
	/* *Cpint2 = *Cpint2 + 1; ERROR*/ // We can't use the const pointer to modift the value
									  // it points to.
	int y;
	const int* pConstY = &y;		// legal- can't use pConstY to modify Y
	int* pMutableY = &y;			// legal- can use pMutableY to modify y
	*pMutableY = 42;
	
	/* Const will also allow us to pretend that a variable is of a different type 	*/
	/* we have to be careful with casting, as it can be used to make mistakes		*/
	const int x = 4;	// x is const, it can't be modified
	const int * pX = &x; // pX can't be modified, and can't modify x via this pointer.
	
	cout << "x = " << x << endl;
	int *pX2 = (int *)pX;	// explicitly casts pX as an int*
	*pX2 = 3;				// result is undefined - since we can't
							// modify x, but we've explicitly changed
							// the type of x.

	cout << "x = " << x << endl; // Prints a 4 - so our trick failed.


	return 0;
}

// vim command
//	:%s/foo/bar/g == find each foo, replace with bar

// vim command
// :%s/foo/bar/gc == find each foo, replace with bar, ask to confirm

// vim command
// :%s/\<foo\>/bar/gc == find only whole words exactly matching foo, change to bar,
// 						 ask for confirmation first.

// vim command
// :%s/foo/bar/gci == find foo (case insensitive) replace with bar

// vim command
// :%s/foo/bar/gcI == find foo (case sensitive) replace with bar
