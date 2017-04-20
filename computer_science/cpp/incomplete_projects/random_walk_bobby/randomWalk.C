#include <iostream>
#include  <sstream>
#include  <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

// assumes that box lives in positive
// x, y, z octant
class Walker
{
    public:
        Walker(int xBoundary, int yBoundary, int zBoundary) 
        {
            xEdge = xBoundary;
            yEdge = yBoundary;
            zEdge = zBoundary;
		
			// watch out - integer division has rules:
			// ie, 5/2 = 2 (not 2.5) - this might lead to unexpected
			// behavior for very small boxes.
			x = xEdge/2;
			y = yEdge/2;
			z = zEdge/2;

            AtEdge = false;
        };

        ~Walker() {};// destructor is empty because no dynamically allocated memory is used

        void Initialize(int startX, int startY, int startZ)
        {
            x = startX;
            y = startY;
            z = startZ;
            if (CheckIfAtEdge(startX,startY,startZ))
            {
                AtEdge = true;
            }
        };


        bool CheckIfAtEdge(int xPos, int yPos, int zPos)
        {
            if( xPos >= xEdge )
            {
                return true;
            }
            else if( yPos >= yEdge )
            {
                return true;
            }
            else if( zPos >= zEdge )
            {
                return true;
            }
            return false;
        };

        bool CheckIfAtEdge()
        {
            return AtEdge;
        };

        void Walk(int xStep, int yStep, int zStep) 
        {
            if( CheckIfAtEdge(xStep+x, yStep+y, zStep+z) == false )
            {
                x = x+xStep;
                y = y+yStep;
                z = z+zStep;
            }
            else if( ( CheckIfAtEdge(xStep+x, yStep+y, zStep+z) == true )&&( AtEdge == false ) )
            {
                x = x+xStep;
                y = y+yStep;
                z = z+zStep;
                AtEdge = true;
            }
			else
			{
				// you can change boundary conditions, or, give each walker a name so that this 
				// message tells you which walker has reached the wall.
				// (give the walker a std::string name member variable, which is set in the
				// constructor, for example).
				std::cout << "INFORMATION: a walker has reached the edge of its grid and will not stop walking." << std::endl;
			}
        };

        int GetX()
        {
            return x;
        };

        int GetY()
        {
            return y;
        };

        int GetZ()
        {
            return z;
        };
    private:
        int x;
        int y;
        int z;
        int xEdge;
        int yEdge;
        int zEdge;
        bool AtEdge;
};

// returns 1 or -1
int takeStep()
{
	// give 'unique' seed
	int rand_i = rand()%2;
	switch(rand_i)
	{
		case 0:
			return -1;
			break;
		case 1:
			return 1;
			break;
		default:
			return 0;
	}
	return 0;
}

// Each walker is initialized with boundaries
// Each walker must be initialized 
// If storage is desired, a separate vector can be defined
// which holds either walkers or walker-states.
// 
// i.e.:
// std::vector<walker> walkerSteps;
// a_walker.Walk(takeStep(), takeStep(), takeStep())
// walkerSteps.push_back(a_walker);
//
// or
//
// std::vector< std::vector< int > > steps;
// std::vector<int> triplet;
// triplet.resize(3);
// triplet[0] = var_i;
// triplet[1] = var_j;
// triplet[2] = var_k;
// steps.push_back(triplet);
//
// accerss with:
// steps[0][0] // the 0th step (first index), x value (second index)


// argc -> argument count (1 + number of arguments, since program name is usually always by default, an argument)
// argv -> argument vector
int main(int argc, char *argv[] )
{

	std::vector<int> gridDimension(3,0); // size of 3, each entry is 0
	
	// argc is the size of the array of character arrays, argv
	// in this case, we pass the three grid-dimensions as an argument to
	// this function.
	
/*  // debug command-line input
	for(int i = 0; i < argc; i++)
	{
		std::cout << "\targv[" << i << "]:" << " " << argv[i] << std::endl;
	}
*/

	if ( argc != 4 ) 
	{
		std::cout << "You gave " << argc-1 << " arguments. Please specify 3 integer grid dimensions as arguments. " << std::endl;
		return -1;
	}
	else
	{
		for(int i = 1; i < argc; i++)
		{
			int tempVal;

			// char-to-int conversion with input stringstream, istringstream
			std::istringstream ss(argv[i]);
			if(!(ss >> tempVal)) std::cout << "Invalid number: " << argv[i] << std::endl;
			gridDimension[i-1] = tempVal; // gridDimensioned indexed: 0, 1, 2 (not 1, 2, 3)
			ss.clear();
			ss.str("");
		}
	}

	std::cout << "Initializing walker with SizeX: " << gridDimension.at(0)
		<< ", SizeY: " << gridDimension.at(1) << ", SizeZ: " << gridDimension.at(2)
		<< std::endl;

	srand((unsigned)time(0));

	// define grid boundary
    int SizeX = gridDimension[0];
    int SizeY = gridDimension[1];
    int SizeZ = gridDimension[2];

    Walker walkie(SizeX,SizeY,SizeZ); // call the walker - and set the grid boundaries in the constructor
    //walkie.Initialize(50,50,50);    // for simplicity - the intial position is by default, near the center of the grid
									  // for a differnt starting point, call Initialize
	std::ofstream outFile("random_walk.txt");

	// print out starting step
    outFile << walkie.GetX() << "\t" << walkie.GetY() << "\t" << walkie.GetZ() << std::endl;

	// if running multiple walkers - they can be done simultaneously
	// with while((!walker_1.CheckIfAtEdge()) && (!walker_2.CheckIfAtEdge()) )
	long long int steps = 0;
    while(!walkie.CheckIfAtEdge()) // once the walker hits any edge, CheckIfAtEdge returns true
    {
		// file size gets very large for large grid.
		// maybe consider only printing out first and last positions + number of iterations
		// for very large grids.

		int var_i = takeStep(); // takeStep is separated from walker, to allow for differnt step sizes
		int var_j = takeStep();
		int var_k = takeStep();

        walkie.Walk(var_i, var_j, var_k); // takes a step in x, y, and z

        outFile << walkie.GetX() << "\t" << walkie.GetY() << "\t" << walkie.GetZ() << std::endl;
		
		if(steps%300==0) std::cout << "Steps Walked: " <<  steps << "     \r" << std::flush;
		steps++;
    }
	std::cout << "Steps Walked: " <<  steps << std::endl;

	std::cout << std::endl;
	outFile.close();
	return 0;
}
