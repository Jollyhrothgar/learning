#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// use -std=c++0x to compile
	template <typename T>
void split (const vector<T>& in, vector<T>& first, vector<T>& second)
{
	first.insert(first.begin(), in.begin(), in.begin() + (in.size() / 2));
	second.insert(second.begin(), in.begin() + (in.size() / 2), in.end());
}

int main()
{
	vector<int> x = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	vector<int> d1, d2;
	split(x, d1, d2);

	cout << "lower half: ";
	for(int i = 0; i < d1.size(); i++)
	{
		cout << d1[i] << " ";
	}

	cout << "\nupper half: ";
	for(int i = 0; i < d2.size(); i++)
	{
		cout << d2[i] << " ";
	}

	cout << endl;
}
