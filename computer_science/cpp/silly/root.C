#include<iostream>
#include <sstream>
#include <vector>

int main(int argc, char* argv[])
{
	std::stringstream blurb;
	blurb << "  *******************************************"<< std::endl;
	blurb << "  *                                         *"<< std::endl;
	blurb << "  *        W E L C O M E  to  R O O T       *"<< std::endl;
	blurb << "  *                                         *"<< std::endl;
	blurb << "  *   Version   5.34/09      26 June 2013   *"<< std::endl;
	blurb << "  *                                         *"<< std::endl;
	blurb << "  *  You are welcome to visit our Web site  *"<< std::endl;
	blurb << "  *          http://root.cern.ch            *"<< std::endl;
	blurb << "  *                                         *"<< std::endl;
	blurb << "  *******************************************"<< std::endl;
	blurb << ""<< std::endl;
	blurb << "ROOT 5.34/09 (v5-34-09@v5-34-09, Jun 26 2013, 17:10:36 on linuxx8664gcc)"<< std::endl;
	blurb << ""<< std::endl;
	blurb << "CINT/ROOT C/C++ Interpreter version 5.18.00, July 2, 2010"<< std::endl;
	blurb << "Type ? for help. Commands must be C++ statements."<< std::endl;
	blurb << "Enclose multiple statements between { }."<< std::endl;

	std::cout << blurb.str() << std::endl;

	unsigned int input_i = 0;
	std::string user_input = "";
	std::string quit_root = ".q";

	while( user_input.compare(quit_root) !=  0)
	{
		std::cout << "root [" << input_i << "] ";
		std::cin >> user_input;
		input_i++;
	}

	return 0;
}
