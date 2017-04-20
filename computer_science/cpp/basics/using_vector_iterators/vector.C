#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

int vector()
{
	vector<double> doub;
	vector<double> doab;

	for(double ii = 0; ii < 12; ii++)
	{
		if(ii<11.0) doub.push_back(ii);
		if((ii<12.0)&&(ii>0.0)) doab.push_back(ii);
	}

	cout << doub.size() << ", " << doab.size() << endl;
	cout << endl;

	vector<double>::iterator j = doab.begin();
	int n = 0;
	double sum = 0;
	for (vector<double>::iterator i = doub.begin(); i < doub.end(); i++)
	{
		cout << *i << ", " << *j << endl;
		if(i == j)
		{
			cout << "The iterators are the same" << endl;
			cout << n << endl << endl;
			n++;
		}

		if(*i < *j)
		{
			cout << "*i and *j can be used in operations, which return sensical results." << endl;
			sum = *i + *j;
			cout << sum  << endl << endl;
		}

		j++;
		if(i >= doab.end())
		{
			cerr << "Bad iteration!!" << endl;
			break;
		}
	}
	return 0;
}
