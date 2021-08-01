// Here, we introduce the concept of a 'virtual function' which may be
// inherited by sub-classes. This header must be guarded, since all of its
// derived classes use it.

// Note that since this is a parent class without instantiation possibility
// (or at least, without any members that can be used in main.cpp, funcitons
// are "inlined". This is a practice of definting very short members in the header
// which will preclude the neccessity of a body.cpp class definition file.
// we're just laying out the structure right here.
#ifndef BODY_H
#define BODY_H

class body
{
	public:
		//virtual = can be overidden by subclass
		//float = return type
		//=0 -> must be overridden - this function cannot be called
		// Note, the absense of a constructor: this class cannot be instantiated
		virtual float GetVolume()  =0;
		virtual float GetSurface() =0;
};

#endif /* BODY_H */
