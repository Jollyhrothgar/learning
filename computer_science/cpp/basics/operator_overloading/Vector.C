#include "Vector.h"

//Define the non-empty constructor
CVector::CVector(float a, float b)
{
	x = a;
	y = b;
}
// Here is where we define what the operator "+" does for objects
// in the CVector class. Notice that we use two C objects in the
// actual definition of this specialized operator member funtion.
// In code, we can simply use "+" to add two CVector objects.
// This function can be called implicitly, using the obj1 + obj2 = obj3
// (addition, as we would expect), or explicitly: obj3 = obj1.operator+ (obj2);
// Note, that without defining an empty constructor, we could not overload
// the addition operator to behave as we would expect for this vector object
// Since, shouldn't we expect the result of addint two vectors to be yet
// another vector? 
CVector CVector::operator+ (CVector param)
{
	CVector temp;
	temp.x = x + param.x;
	temp.y = y + param.y;
	return (temp);
}

CVector::~CVector(void) {};


