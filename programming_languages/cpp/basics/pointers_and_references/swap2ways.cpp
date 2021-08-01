#include <iostream>
using namespace std;

// Note how we can use funtions to modify variables by passing
// references to the variables, or pointers to the variables.
// and also note how " " spaces do not make a shit of differnece.
void swap1(int&,int&);
void swap2(int*,int*);

int main()
{
	int a = 1;
	int b = 2;
	cout << "a = " << a << ", b = " << b << endl;
	cout << "swapping..." << endl;
	swap1(a,b);
	cout << "a = " << a << ", b = " << b << endl;
	cout << "swapping..." << endl;
	swap2(&a,&b);
	cout << "a = " << a << ", b = " << b << endl;
	return 0;
}

void swap1(int& x1, int &y1)
{
	int temp = x1;
	x1 = y1;
	y1 = temp;
}

void swap2 (int *x2, int* y2)
{
	int temp = *x2;
	*x2 = *y2;
	*y2 = temp;
}
