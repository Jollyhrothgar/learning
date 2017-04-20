#include<iostream>
#include<cmath>
#include<fstream>
#include "Mike_Math.h"
#include <fstream>
using namespace std;


int main()
{
	long double bet;
	long double roll;
	long double not_roll;
	long double total_dice;
	long double set;
	cout << "How many dice are in play?\n-> ";
	cin >> total_dice;
	cout << endl;
	cout << "How many die of the same face are known (including wild) \n-> ";
	cin >> roll;
	cout << endl;
	cout << "How many die are not what you want \n-> ";
	cin >> not_roll;
	set = (total_dice - roll - not_roll);
	
	cout << endl;
	cout << "Odds are your chances to win if the next player calls bullshit on your bet.\n";
	cout.precision(3);
	cout << "Number of known dice: " << (roll + not_roll) << endl;
	cout << "Unknown dice: " << set << endl;
	cout << "Effective game reduced to " << set << " dice with all dice unknown." << endl;
	cout << "------Odds------" << endl;
	for(bet = 0.0; bet <= set; bet++)
	cout << "Bet: " << bet + roll << " Odds: " << Proll(bet,set) << endl;
	return 0;
}	
