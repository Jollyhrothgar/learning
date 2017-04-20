class CVector
{
	public:
		float x, y;	
		CVector () {};// Weird, eh? This is an 'empty
						// constructor. It allows us to
						// declare uninitialized objects
						// such that we can copy one object
						// to another uninitialized object
		CVector (float, float);
		CVector operator + (CVector);	// Overloads the "+" operator 
		// adding meaning when used for between two CVectors.
		// operator+ is actually a function, only it is called differenly
		// than other memberfunctions (say like CVector.Add();, hypothetically).
		// in this instance, we can implicitly call the funciton, such that it
		// looks and behaves like an operator. It is in fact a funciton, of type
		// CVector, which returns a C vector object, and takes a CVector
		// object as an argument.
		~CVector(void);
};
