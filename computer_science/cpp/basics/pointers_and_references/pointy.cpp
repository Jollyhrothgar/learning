#include <iostream>
using namespace std;

int main()
{
	// a pointer stores the memory address of a variable.
	// referencing a pointer will give the value at the pointer's memory addrs.
	// referencing a variable will give the variable's memory address.
	
	/* Pointers */
	int a = 5;	// declare an integer
	cout << "\n\nThis program will go through the differences between pointers"
		<< endl << "and references. We will work with an integer, \"a\", which"
		<< endl << "is set to a value of " << a << endl;

	int * pi1;	// declare a pointer to an integer
	int* pi2;	// another pointer to an integer
	int *pi3;	// etc
	int * pi4;	// Not how spacing doesn't matter.
	int * pi5;
	
	pi1 = &a;	// correct use of pointer -> assigns address of a to pi1
				// here, we have declared a pointer of type
				// "pointer to int" who's value was uninitialized, but
				// has now been initialized to the address of object a (which
				// must be an integer, due to the type declaration). Note that
				// pi1 could be assigned to point to another integer with a
				// reassignment. However, a pointer can point EITHER to an
				// object, or, to nothing. A pointer is either declared
				// statically, in which case it MUST be assigned a memory
				// address, OR it can be assigned dynamically, with the "new"
				// operator.
	
	//incorrect use of pointer -> pi2 = a woudl assign an int type to an *int
	//type, and the compiler should complain. Except for below-->
	
	pi3 = 0;	// assigns pi3 to the NULL memory address
	pi4 = NULL;	// same thing ^^.
	
	/* References */
	int &ri1 = a;	// Note, no uninitialized references can be declared.
					// Thus, we can't declare references and set them later
					// they must be set at the moment of instantiation.
					// This declaration says "ri1 is an object of type
					// "reference to int" referring to a. Note that this
					// reference to a is unique to ri1, in that ri1 can never
					// be reassigned to reference another variable. In that
					// ri1 is like a const pointer. A reference also differs
					// from a const pointer, since we cannot have null
					// references. A reference must ALWAYS reference something.
					// A reference may be assinged to a dereferenced
					// null pointer. This is bad. The null address can contain
					// fucking ANYTHING.
	
	// Here is a bad reference that will compile, but will produce a seg
	// fault when run. Don't do it!!
	// int &ri2 = *pi3;
	// cout << "Here's a bad reference that will compile: " << ri2 << endl;

	// So, what the fuck is the difference? Both * and & allow us to indirectly
	// access data, of some type, by storing memory addresses. The big
	// difference is in implimentation.
	
	/*											*/
	/* Look at the following implimentation:	*/
	/*											*/

	cout << "pi1 does not derefernce automatically: " << pi1 << endl;	
	/* outputs address of a */
	
	cout << "ri1 automaticaly dereferences: " << ri1 << endl;	
	/* outputs actual value a */
	
	// So, we find that pointers must be 'dereferenced' with *
	// However, we can get at the memory address stored with ri1
	// Observe:
	
	cout << "Dereferenced Pointer Value: " << *pi1 << endl;
	cout << "Reference Value: " << &ri1 << endl;
	// So, pointers need "*" to dereference, but a reference is automatically
	// dereferenced. It can be 'rereferenced' by applying & again.
	
	// if we want memory value from a pointer or reference:
	cout << "Memory value of pi1: " << pi1 << endl;
	cout << "Memory value of ri1: " << &ri1 << endl;
	
	// if we want value of a variable that is pointed to or referenced by
	// a pointer or reference:
	cout << "Value of variable pointed to: " << *pi1 << endl;
	cout << "Value of variable referenced: " << ri1 << endl << endl;

	/* Why pointers and references? Well, often times, we need a function
	to access variables or objects directly. When we pass a variable or object
	to a function, we actually make a copy of that passed argument. Any
	modifications to the argument within the function are applied to a copy
	of that argument automatically made when the function is instantiated.
	So, modifications are applied to a copy of the arguement, and then 
	the function returns something. But, what if we need the function to
	actually modify the arguments passed in to it? Then, we need to tell
	the function where to look - using pointers, or using references.
	this might have special consequences for overloading operators so that
	you can define expected behaviours (from polymorphism) (such as indexing
	by one, where we desire to index by a unit of the class so that
	class1++; has meaning.
	
	We can do so via pointer OR reference. */ 


	return 0;
}

