#include <string>
#include <sstream>
#include <iostream>
#include <iterator>
class Person {
	std::string ID;
	std::string name;
	std::string address;
	std::string phone;
	public:
	Person() {}

	void show() const {
		std::cout << "Person created with ID " << ID << " and phone " << phone << '\n';
	}

	friend std::istream& operator>>(std::istream& is, Person& p) 
	{
		getline(is, p.ID);
		getline(is, p.name);
		getline(is, p.address);
		getline(is, p.phone);
		return is;
	};
};

int main()
{
	std::istringstream test("529173860\n"
			"Dick B. Smith\n"
			"879 Maple Road, Centralia, Colorado 24222\n"
			"(312) 000-1000\n"
			"925173870\n"
			"Harry C. Anderson\n"
			"635 Main Drive, Midville, California 48444\n"
			"(660) 050-2200");
	Person p;
	while(test >> p) // proper input loop
	{
		p.show();
		std::cout << std::endl;
	}
}
