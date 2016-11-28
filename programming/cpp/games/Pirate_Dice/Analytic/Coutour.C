#include<iostream>
#include<cmath>
#include<fstream>
#include "Mike_Math.h"
#include <fstream>
using namespace std;
int main()
{
	ofstream outFile;
	outFile.open("Contour.d");
	long double bet;
	long double roll;
	long double not_roll;
	long double total_dice;
	long double set;
	

	for(bet = 0.0; bet <= set; bet++)
	outFile << "Bet: " << bet + roll << " Odds: " << Proll(bet,set) << endl;
	return 0;
}
