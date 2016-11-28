#include<iostream>
#include<vector>
using namespace std;

// split steps function - split into vertical + horizontal steps.
template <typename T>
void dVsplit(vector<T>& splitme, vector<T>& firsthalf, vector<T>& lasthalf)
{
	cout << "Funct 1\n";
	int i = 0;
	cout << "Funct 2\n";
	if((splitme.size())%2!=0)
	{
		cout << "Warning, the vector you're trying to split has an odd number of entries." << endl;
		int half = (splitme.size() + 1)/2;
		for(typename vector<T>::iterator it = splitme.begin(); it<splitme.end(); it++)
		{
			if(i < half)
			{
				firsthalf.push_back(*it);
			}
			else
			{
				lasthalf.push_back(*it);
			}
			i++;
		}
	}
	else
	{
		cout << "ElseFunct 1\n";

		int half = (splitme.size())/2;
		cout << half << endl;
		cout << "ElseFunct 2\n";
		for(typename vector<T>::iterator it = splitme.begin(); it<splitme.end(); it++)
		{	
			
			cout << "ElseFunct " << i << endl;
			if(i < half)
			{
				firsthalf.push_back(*it);
			}
			else
			{
				lasthalf.push_back(*it);
			}
			i++;
		}
	}
	cout << "Splitting finisehd. Check: V1.size() -> V2.size() + V3.size()" << endl;
	cout << splitme.size() << " -> " << firsthalf.size() << " + " << lasthalf.size() << endl;
}


int main()
{
	cout << "Line 1\n";
	vector<double> v1;
	cout << "Line 2\n";
	for(double i = 0; i<10; i++) v1.push_back(i);
	cout << "Line 3\n";
	vector<double> v2;
	cout << "Line 4\n";
	vector<double> v3;
	cout << "Line 5\n";
	dVsplit(v1,v2,v3);
	cout << "Line 6\n";
	return 0;
}

