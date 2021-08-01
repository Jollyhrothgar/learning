#include<iostream>
int main()
{
	// << left associative operator, will use stuff to left as operand if possible
	// std -> namespace
	// parantheses clarify order of operations
	// type of cout is of type std::ostream
	// std::endl is a manipulator - the key property of manipulators
	// is that writing one in a stream, manipulates the stream.
	// in this case, the right hand operand of << must be either
	// blank, or a stream manipulator.
	// This entire expression yields std::cout as its return type,
	// which has the effect of writing Hello, World! on the standard
	// output stream.
	(std::cout << "Hello, World!") << std::endl;
	// The semicolon at the end of the statement has the effect of
	// disregarding the return value of std::cout, since all we cared
	// about was the effect of printing to the output stream. In this
	// sense, all functions, variables, or anything written must have
	// a return value or type, and we always ultimately disregard
	// everything that was not saved or put somewhere non-volitile.

	// When using names from the standard library (std) we need to
	// specify globally or locally. Specifying the namespace locally
	// avoids naming collisions.

	// Curly brackets specify another scope. Named items in a scope
	// cannot be used elsewhere, unless declared globally.

	// Spaces, or tabs, are only used to improve readablilty. The only
	// neccesity of spaces is to keep adjacent symbols from running
	// together.

	// Three entities are not free form.
	// 1) string literals - characters enclused in double quotes, may not span lines.
	// 2) #include name - must appear on its own line, save for comments
	// 3) commends end after current line.

	// C++ has two kinds of types. Those built into core language (such as int)
	// and those defined outside core language (such as std::ostream)
	// special string literals: \n = newline
	//							\t = tab
	//							\b = backspace
	//							\" = double quotes
	//							\' = single quote
	//							\\ = includes \ in string
	return 0;
}
