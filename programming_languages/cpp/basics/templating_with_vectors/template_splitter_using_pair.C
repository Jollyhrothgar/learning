#include <vector>
#include <iostream>
#include <utility>
using namespace std;

// compile with g++ -std=c++0x

template<class T>
pair<vector<T>,vector<T>> split(const vector<T>& vin)
{
	typename vector<T>::const_iterator halfpoint=vin.begin()+vin.size()/2;
	return make_pair(vector<T>(vin.begin(),halfpoint),vector<T>(halfpoint,vin.end()));
}

int main()
{
	// Test vector
	vector<int> x;
	cout << "Seed vector: ";
	for(size_t i = 0; i < 13; i++)
	{
		x.push_back(i + 1);
		cout << x.back() << " ";
	}
	cout << endl;
	
	pair <vector<int>,vector<int>> mypair=split(x);
	cout << "lower half: ";
	for(size_t i = 0; i < mypair.first.size(); i++) cout << mypair.first[i] << " ";
	cout << endl;
	
	cout << "upper half: ";
	for(size_t i = 0; i < mypair.second.size(); i++) cout << mypair.second[i] << " ";
	cout << endl;
}
