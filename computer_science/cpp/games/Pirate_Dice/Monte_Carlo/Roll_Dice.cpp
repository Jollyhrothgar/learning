#include<time.h>
#include<stdlib.h>
#include<cmath>
#include<iostream>
#include<fstream>
#define DICE_LEFT 40
using namespace std;

int main(void)
{
	//int DICE_LEFT = 10;
	int Dice[DICE_LEFT]={0};//Index 0-(DICE_LEFT-1) - array with number of dice, value is face of die.
	int Counter[6] = {0};	//Each bin of counter is for a die face. 0 = 1, 1 = 2, etc.
	int i = 0;		//indexer 1
	int n = 0;		//indexer 2
	int face = 0;		//var holds face value
	float numDice = 0;	//indexer 3
	float numWin = 0;	//var holds number of wins
	int numLose = 0;	//var holds number of losses
	float Games = 1000000;	//var holds number of games to play
	
	srand( time(NULL) );
	
	//cout << "What value: ";	//Input face to guess (only matters if its 1)
	//cin >> face;
	face = 5;
	for(numDice = 1; numDice < (DICE_LEFT+1); numDice++)	//Plays a set of games for each guess
	{	
		numWin = 0;	// Must initialize here, for each set of games
		numLose = 0;	// Must initialize here for each set of games
		for(n = 0; n < Games; n++)
		{
			// Fill Dice
			for(i = 0; i < DICE_LEFT; i++ ) Dice[i] = 0;
			for(i = 0; i < 6; i++) Counter[i] = 0;
			for(i = 0; i < DICE_LEFT; i++)
			{
				Dice[i] = rand()%6 + 1;
				Counter[Dice[i] - 1] = Counter[Dice[i] - 1] + 1;
			}
			if(numDice <= (Counter[face] + Counter[0]))
			{
				numWin++;
			}
			else
			{
				numLose++;
			}
		}
		cout << (numWin/Games)*100 << "%" << endl;
		//cout << "When you guess " << numDice << " " << face + 1 << "'s,"
	     	//<< " you will win " << (numWin/Games)*100.0 << "%" << " of the"
	     	//<< " time.\n";
	}	
	return 0;
}
