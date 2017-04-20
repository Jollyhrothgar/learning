#include "Mike_Math.h"
long double binomC(long double n,long double k)
{
	//
	// Binomial coefficient, (n,k) means n choose k
	//
	//			 k
	//	[n]	   -----  n - (k - i)
	//	[k] ==	| |  -------------
	//			i=1		   i
	//
	//
	long double i = 0;
	long double result;
	long double top = 1.0;
	long double bot = 1.0;
	if((n<0)||(k<0))
	{
		return 0.0;
	}
	else if(n<k)
	{
		return 0.0;
	}
	else if(k<=n)
	{
		// Used: multiplicative formula
		// en.wikipedia.org/wiki/Binomial_coefficient
		for(i = 1; i < (k+1);i++)
		{
			top = (n - (k - i))*top;
			bot = bot*i;	
		}
		result = top/bot;
		return result;
	}
	else
	{
		return 0.0;
	}
}
