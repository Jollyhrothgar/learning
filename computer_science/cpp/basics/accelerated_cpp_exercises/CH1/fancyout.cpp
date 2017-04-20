#include<iostream>
#include<string>
int main()
{
	std::cout << "Please enter your first name: ";
	std::string name;
	std::cin >> name;

	// notice how we can use "+" to build one line of an output string.
	// This is called concatination. "+" works for two strings, a string
	// and a string literal, but not two string literals. (probably due to
	// null termination) + is overloaded. Const variables can never change
	// it may make reading a program easier to see which variables can
	// change and which must be forced to remain the same.
	// '=' implies we are explicitly passing a value
	// () implies that we are constructing a value.
	// IE, spaces is a string variable, but rather than passing a value to it,
	// we will construct a value, which will be given to it.

	// Look - we're declaring a string object, named spaces, using a constructor
	// that's what we literally mean. How a variable is constructed depends
	// entirely on that variable.

	// Here we use the integer constructor, rather than the integer copier
	// which would be implimented: int myint = 5;
	int myint(5);
	std::cout << myint << std::endl;
	
	//concatination of strings
	const std::string greeting = "Hello, " + name + "!";
	
	// constructing a string from an object's memberfunction and a character literal.
	// A character-literal is entirely distinct from a string literal. A character
	// literal is always enclosed in single quotes, a string literal is always enclosed
	// in double quotes. The type of a character literal is the built in type, char.
	// The type of a string literal is complicated. A character literal represents a 
	// single characer, special characters work the same way, but with single quotes.
	// In this case, when we contruct a string from an integer value, and a literal
	// character value, the result is a string made from that character repeated an
	// that integer number of times.
	const std::string spaces(greeting.size(), ' ');
	const std::string second = "* " + spaces + " *";

	//build first and fifth lines of the output
	const std::string first(second.size(),'*');

	//write it all
	std::cout<< std::endl;
	std::cout<< first << std::endl;
	std::cout<< second << std::endl;
	std::cout<< "* " << greeting << " *" << std::endl;
	std::cout<< second << std::endl;
	std::cout<< first << std::endl;
	
	return 0;
}

// Special character types.
// char - the usual
// wchar_t - holds characters that are larger, such as japanese.

/*** General Expressions ***/

// int s; 
// char c; 
// istream = is; 
// ostream = os;
//

// std::sting s;		Defines empty string type, s.

// std::string t = s;	defines another string t, holding a copy of s--s can be string

// std::string z(n,c);	initializes a string z to contain n copies of character c.

// os << s  			Writes characters contained in s, without formatting changes to 
//						output stream denoted by os. The result of the expression is "os".

// is >> s  			Reads and discards characters from stream denoted by is 
//						until encountering a character that is not whitespace. Then, 
//						successively reads characters from <is> to s, overwriting whatever 
//						values s might have had until next whjtespace character is read. 
//						The result is 'is'.

// s + t				The result of this expression is a std::string that contains a copy
//						of the cahracters in s, followed by the characters in t. Either s or
//						t, but not both, may be a string literal or a value of type char.

// s.size()				Number of characters in s.

/*** 3 Ways to Define Variables ***/
// 1) Define variable with explicit initial value
// ex:
// 		std::string hello = "Hello";

// 2) Construct the variable (according to type and given expressions)
// ex:
//		std::string stars(100,'*');

// 3) Define variable with implicit initialization (depends on type).
// ex:
// 		std::string name;

// Scope: variables defined in a block are only kept until the end of the block '}'
// at which point they are discarded from memory.

// Const ensures a variable that does not change.
