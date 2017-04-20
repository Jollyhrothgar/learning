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

// Probability that at least _betdice of one face is showing, out of _totdice total dice
// if only probability is of interest, can be recovered by changing 1/6 -> 2/6 and 5/6 -> 4/6
// to get odds for a roll including wild dice.

// Proll(#dice to bet, #dice on table) = probability of winning
long double Proll(long double _betdice, long double _totdice)
{
	long double i;
	long double probability = 0.0;
	if(_betdice > _totdice)
	{
		return 0.0;
	}
	else
	{
		for(i = _betdice; i <= _totdice; i++)
		{
			probability += binomC(_totdice,i)*pow((2.0/6.0),i)*pow((4.0/6.0),(_totdice-i));
		}
		return probability;
	}
}
