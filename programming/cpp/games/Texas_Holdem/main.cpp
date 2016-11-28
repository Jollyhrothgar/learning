#include<iostream>
#include<vector>
#include "Mike_Math.h"
#include "Card.h"
using namespace std;

int main()
{

	/*PlayerHand hand[2];*/

	cout << "\n\n This program will calculate odds of winning poker.\n";
	
	cout << endl;
	return 0;
}

// Notes:
// Proabably handInit() should be a function used to initalize
// a poker hand

//	Equivalence Arrays
//	
// 	Values:
//		Human:		2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
//		Program:	2, 3, 4, 5, 6, 7, 8, 9, 10, 11,   12,    13,   14		
//	Suits:
//		Human:		Hearts, Spades, Clubs, Diamonds
//		Program: 	'h',	's',    'c',   'd'

// poker hands: h,s,d,c (Heart, Spade, Diamond, Club)
// I'm considering implimenting either a pair of arrays
// Perhaps the card's instantiation can be separate from
// how the card keeps track of its relative suit and value

// For example, card might never be initialized inside main
// maybe card would only be initialized in Deck?

// But, then again, as the author of the analysis, I don't
// need to really concern myself with information hiding,
// copy constructors or other.

// But, I do want to be able to play several rounds of poker
// or maybe just set up poker in such a way as to play from 
// the terminal.

// The suit does not determine value, unless suits match.
// Also, we need a means of determining kickers, etc.

// I believe the best way would be nested for loops to compare
// each card to every other card in the hand+table cards and
// determination of 'best' hand will require swapping of
// hands.

// I think a hierarchical decision tree is the way to go,
// where the mots general hand is found. Then, that will
// break into a lower tree to determine best combination.
