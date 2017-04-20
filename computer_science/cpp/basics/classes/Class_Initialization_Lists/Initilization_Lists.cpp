#include <iostream>
//
//	This program is designed to experiment with the class structure
// 	I've seen in the classes derived from SubsysReco. The inheritance
//	seems to proceed: Fun4AllBase->SubsysReco->analysis class
//	
//	While AnaPHPythia seems to adhere to initializing everything with
// 	The analysis module file's name, this routine only initializes the
// 	output file's name. I could modify this to work correctly, perhaps.
//


// The concept explored here is an initialization list. Since all parent
// classes must be constructed so that they can make a child class, if
// any parent class needs a non-empty constructor, we have to use an initialization
// list to construct a parent class correctly. Not only this, but the FIRST instance
// the parent class is needed, it must be initialized, even if its needed ONLY because
// its child class is called.
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
