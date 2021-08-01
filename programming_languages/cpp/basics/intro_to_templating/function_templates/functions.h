#ifndef FUNCTIONS_H
#define FUNCTIONS_H
template<class T>
void swap_values(T& var1,T& var2)
{
	T temp; // T is standin for type
	temp = var1;
	var1 = var2;
	var2 = temp;
}
#endif
