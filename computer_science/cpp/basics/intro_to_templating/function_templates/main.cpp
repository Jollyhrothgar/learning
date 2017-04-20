#include<iostream>
#include<string>
#include "stdio.h"
#include "functions.h"
int main()
{
	int int1 = 1;
	int int2 = 2;
	char a = 'a';
	char b = 'b';
	std::string st_var1 = "Howdy Pahdna!";
	std::string st_var2 = "See ya Cowpoke!";
	
	std::cout << "Before Swap: ";
	printf("int1 = %i, int2 = %i\n",int1,int2);
	std::cout << "After Swap: ";
	// can use swap<int>(int1,int2), but compiler
	// autmatically selects appropriate verion otherwise
	// for safety, you can directly specify the operand
	// types with <type> after swap_values
	swap_values<int>(int1,int2);
	printf("int1 = %i, int2 = %i\n",int1,int2);
	
	std::cout << "Before Swap: ";
	printf("char1 = %c, char2 = %c\n",a,b);
	std::cout << "After Swap: ";
	swap_values(a,b);
	printf("char1 = %c, char2 = %c\n",a,b);
	
	std::cout << "Before Swap: ";
	std::cout << st_var1 << ", " << st_var2 << std::endl;	
	swap_values(st_var1,st_var2);
	std::cout << "After Swap: ";
	std::cout << st_var1 << ", " << st_var2 << std::endl;	
	
	return 0;

}
