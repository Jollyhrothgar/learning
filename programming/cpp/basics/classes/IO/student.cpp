#include <iomanip>
#include <string>
#include <iostream>
#include <sstream>
#include <iterator>
class student
{
	public:
		string name;
		int id;
		double fees;
		//Other member functions & constructors
		friend ostream& operator<< (std::ostream&, const student&);
		friend istream& operator>> (std::istream&, student&);
};
ostream& operator<<(std::ostream& out, const student& s)
{
	using namespace std;
	out << setw(20) << left << s.name  << ' '
		<< setw(7)  << left << s.id    << ' '
		<< setw(7)  << setprecision(2) << fixed << s.fees;
	return out;
}
istream& operator>>(std::istream& input, student& s)
{
	getline(input, s.name, ','); //read name
	input >> s.id;                    //read id
	input.ignore();
	input >> s.fees;                  //read fees
	input.ignore(numeric_limits<std::streamsize>::max(), '\n');
	return input;
}
