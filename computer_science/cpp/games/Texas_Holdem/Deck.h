#ifndef DECK_H
#define	DECK_H
#include<iostream>
#include<vector>
#include "Card.h"
// Create an instance of a deck of cards
// Vectors should be used inside main to store dealt hands
// and store the flop.
class Deck
{
	public:
		// Create a deck of cards - should be in order
		Deck();
		~Deck() {};

		// Shuffle the deck
		void Shuffle();

		// need member funciton to deal a card
		Card Deal_Card();
};
#endif
