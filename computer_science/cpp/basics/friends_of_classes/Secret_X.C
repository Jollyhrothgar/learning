#include "Secret_X.h"
Secret_X::Secret_X()
{
}

Secret_X::~Secret_X()
{
}

void Secret_X::init_X(int value)
{
	x = value;
}

int read_x(Secret_X temp)
{
	return temp.x;
}

