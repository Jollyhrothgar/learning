#include "Card.h"
Card::Card(int value, char suit)
{
	// HEART, SPADE, DIAMOND, CLUB 
	switch (suit)
		// Hearts
		case 'h':
			SUIT = suit;
		// Spades
		case 's':
			SUIT = suit;
		// Diamonds
		case 'd':
			SUIT = suit;
		// Clubs
		case 'c':
			SUIT = suit;
		default:	
		{
			std::cout << "You did not choose a supported suit\n";
			std::cout << "You must choose: h = hearts, s = spades, d = diamonds, or c = clubs\n";
			std::cout << "You should end this session and have a look at your source code.\n"
			SUIT = 'E';
		}
	// 2,3,4,5,6,7,8,9,10,11=Jack,12=Queen,13=King,14=Ace
	if((value<=2)||(value>=14))
	{
		VALUE = value;
	}
	else
	{
		std::cout << "You did not choose a supported value\n";
		std::cout << "You input a value of " << value << ".\n"
		std::cout << "You must choose \"value\" in range: 2 <= value <= 14; where 11-14 -> J,Q,K,A\n";
		std::cout << "You should end this session and have a look at your source code.\n"
		VALUE = 0;// constrain range
	}
}

