#include <vector>
#include <iostream>
using namespace std;

// template for no C++11, erasure

	template<typename T>
vector<T> split(vector<T> &in, vector<T> &v1, vector<T> &v2)
{
	typename vector<T>::iterator midpoint = in.begin() + in.size() / 2;
	vector<T> v2(midpoint, in.end());
	vector<T> v1(in.begin, midpoint);
}

int main()
{
	vector<int> x;
	for(size_t i = 0; i < 10; i++)
		x.push_back(i + 1);
	
	vector<int> out1;
	vector<int> out2;
	split(x,out1,out2);

	cout << "lower half: ";
	for(size_t i = 0; i < out1.size(); i++)
		cout << out1[i] << " ";

	cout << "\nupper half: ";
	for(size_t i = 0; i < out2.size(); i++)
		cout << out2[i] << " ";

	cout << endl;
}
