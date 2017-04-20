#include <iostream>
using namespace std;
// Pointers and Arrays are completely, totally linked at the hip. A pointer is not a compound data structure.
// Simply, a pointer will store an address in memory. Memory is allocated in heaps in contiguous chunks. If we
// wished, we could take a pointer, output the value it holds, and index its address by one, and read out the next
// value. Arrays represent a list of objects, each object stored in contiguous chunks of memory. When an array is
// referenced, it will return the address of its first data member. If we set a pointer to this address, we could
// index the pointer and read out and/or modify everything in the array, since we know that the data is contiguous.
// However, when we declare an array, we are a data list, whose first member's address is protected - as a const.
// Thus, while we can set a pointer to an array (effectively, setting the pointer to point to the address of the first
// member in the list of data), we cannot set an array to a different address.
//
// Arrays can be thought of as const pointer types. [] is a dereferece offset operator.
// 
// 1. pointer + 1 returns the memory, one increment above the memory of pointer.
// 2. *(pointer + 1) returns the value stored one increment above the address of the pointer
// 3. &Array[i] returns the address of the ith list variable. (indexing starts at 0)
//
// Below, we set p to the address of the first array member. Then, we access various elements of the array
// with pointer arithmatic.
int main ()
{
	int numbers[5];		// std declaration of array
	int * p;			// std declaration of integer pointer
	p = numbers;		// initialize p with address of first member of numbers
	*p = 10;			// set value at p to 10	(equivalent-> numbers[0] = 10, which is equivalent to
						// saying "take my const pointer numbers, don't change the address, and dereference it
						// setting the new value to 10.
 	p++;				// increment memory address of p by 1 (now p points to address that stored numbers[1]
	*p = 20;			// set numbers[1] to 20
	p = &numbers[2];	// update address of p with address of numbers[2]
	*p = 30;			// set numbers 3 to 30
	p = numbers + 3;	// set p to address of &numbers[0]+3, or, &numbers[3]
	*p = 40;			// set value of numbers[3]
	p = numbers;		// resets p back to &numbers[0]
	*(p+4) = 50;		// references the 5th data container of numbers, numbers[4] and sets value to 50.
						// Note, at this point, p is set to first member (0)
	
	for (int n=0; n<5; n++)
	{	
		cout << numbers[n] << ", ";
	}
	cout << endl << numbers << endl;
	cout << p << endl;
	return 0;
}
