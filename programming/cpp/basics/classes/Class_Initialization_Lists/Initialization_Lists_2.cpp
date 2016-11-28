#include <iostream>
// The concept explored here is an initialization list. Since all parent
// classes must be constructed so that they can make a child class, if
// any parent class needs a non-empty constructor, we have to use an initialization
// list to construct a parent class correctly. Not only this, but the FIRST instance
// the parent class is needed, it must be initialized, even if its needed ONLY because
// its child class is called.
// 
// We can also use initialization lists to initialize member data of the class itself.

//																	//
//--------------Initialization List Example 1-----------------------//
//																	//

// initialization example - QUX
// The constrcutor is invoked by giving the name of the object to be constructed
// rather than the name of the class. 

class Qux
{
	public:
		Qux() : _foo("initialize foo to this!") { }
		// This is almost equivalent to
		// Qux() {_foo = "initilize foo to this!";}
		// but without the extra call to construct and empty string
		void getFoo() { std::cout << _foo; }
	private:
		std::string _foo;
};

//																	//
//--------------Initialization List Example 2-----------------------//
//																	//

//If there are multiple fields (the area
// after the colon in the constructor), then the names of the objects being initialized
// should appear in the order the are declared in the class (and after any parent
// constructor call).
class Baz1
{
	public:
		Baz() : _foo("initialize foo first"), _bar("then bar") {}
	private:
		std::string _foo;
		std::string _bar;
};


//																	//
//--------------Initialization List Example 3-----------------------//
//																	//

// The constructor will also know what to do regarding scope, if you use a variable
// with a given name to initialize both a member and a parent class constructor with
// the same value. The constructor knows how to figure out which variable belongs
// to the class member funciton, and what variable belongs to the object.
		
class Class1
{
	public:
	Class1(int x)
	{
			std::cout << "Class1's Constructor" << " called with: " << x << std::endl;
			myspecialint = x;
	}
	private:
	int myspecialint;
};

class Class2 : public Class1
{
	public:
	Class2() : Class1(10)	// Once class 2 is called, compiler checks for parents
	{						// Since Class2's parent is Class1, we have to use an
							// initialization list here.
		std::cout << "Class2's Constructor" << std::endl;
	}
};

class Class3 : public Class2
{
	public:
	Class3()
	{
		std::cout << "Class3's Constructor" << std::endl;
	}
};

int main()
{
	std::cout << "Creating instance of Class3" << std::endl;
	Class3 FOOBAR;
	return 0;
}

// Object Class2 gets constructed in two stages. First, the Class1 constructor is
// invoked. We can see this literally with the output - we made only an object
// of Class2, but when we called it, Class2's constructor was called AFTER Class1's
// constructor.
