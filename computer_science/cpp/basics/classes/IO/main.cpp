#include "student.cpp"
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>
const char* filename = "./students.txt";

int main()
{
	typedef ostream_iterator<student> output;
	ifstream studentfile(filename);
	vector<student> names;
	student input;
	while(studentfile >> input)
		names.push_back(input);
	cout << "Read " << names.size()
		<< " students successfully\n";
	copy(names.begin(), names.end(), 
			output(cout, "\n"));
	cout.flush();
	return 0;
} 

