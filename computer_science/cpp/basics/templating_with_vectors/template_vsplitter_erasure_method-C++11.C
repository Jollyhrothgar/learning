#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// use -std=c++0x to compile
	template<typename T>
vector<T> split(vector<T> &in)
{
	auto midpoint = in.begin() + in.size() / 2;
	vector<T> v(midpoint, in.end());
	in.erase(midpoint, in.end());
	return v;
}

int main()
{
	vector<int> x = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

	auto x_upper = split(x);

	cout << "lower half: ";
	for(auto &i : x)
		cout << i << " ";

	cout << "\nupper half: ";
	for(auto &i : x_upper)
		cout << i << " ";

	cout << endl;
}
