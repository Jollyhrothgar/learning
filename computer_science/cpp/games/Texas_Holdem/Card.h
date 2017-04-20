#ifndef CARD_H
#define CARD_H
#include<string>
class Card
{
	protected:
		char SUIT;
		int VALUE;
		
	public:
		Card(int,char);
		~Card() {};
};
#endif
