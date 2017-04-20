#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip> // setprecision, setw 
#include <cmath>   // fmod
using namespace std;

const int GRID_X_DIMENSION = 100; //3^6
const int GRID_Y_DIMENSION = 100; //3^6
const int GRID_Z_DIMENSION = 100;
const int MULTIPLICITY = 1; //Number of Walkers in each starting grid
double boundary[GRID_X_DIMENSION][GRID_Y_DIMENSION];

void makeBoundary()
{
}

bool checkBoundary(int x, int y, int z)
{
	if ( z >= (GRID_Z_DIMENSION - 1))
	{
		return true;
	}
	else if ( z <= 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int whichBoundary(int x, int y, int z)
{   
	if ( z >= (GRID_Z_DIMENSION - 1))
	{
		return 1;
	}
	else if ( z <= 0)
	{
		return 0;
	}
	else
	{
		return (-1);
	}
}

double walker(int x, int y, int z) //runs MULTIPLICITY walkers for one grid point
{
	double average;
	average = 0;
	for(int k = 0; k < MULTIPLICITY; k++)
	{
		//create random walk until we hit a boundary
		//int initialX = x;
		//int initialY = y;
		int currentX = x;
		int currentY = y;
		int currentZ = z;

		int moveCode;


		bool hitIt = false;


		do
		{
			if(checkBoundary(currentX, currentY, currentZ))
			{
				break;
			}
			else
			{
				moveCode = (rand()%6); //0, 1, 2, 3, 4, 5 = +y, +x, -y, -x, +z, -z
				switch(moveCode)
				{
					case 0: //pos-y
						{
							if(currentY == GRID_Y_DIMENSION-1)
							{
								currentY = 0;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							else
							{
								currentY++;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							break;
						}
					case 1: //pos x
						{
							//add If statement for periodic boundary conditions. Wrap-around or reflect?
							if(currentX == GRID_X_DIMENSION-1)
							{
								currentX = 0;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							else
							{
								currentX++;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							break;
						}
					case 2: //neg y
						{
							if(currentY == 0)
							{
								currentY = GRID_Y_DIMENSION-1;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							else
							{
								currentY--;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							break;
						}
					case 3: //neg x
						{
							//add If statement for periodic boundary conditions. Wrap-around or reflect?
							if(currentX == 0)
							{
								currentX = GRID_X_DIMENSION-1;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							else
							{
								currentX--;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							break;
						}
					case 4: //pos-z
						{
							if(currentZ == GRID_Z_DIMENSION-1)
							{
								currentZ = 0;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							else
							{
								currentZ++;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							break;
						}
					case 5: //neg-z
						{
							if(currentZ == 0)
							{
								currentZ = GRID_Z_DIMENSION-1;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							else
							{
								currentZ--;
								hitIt = checkBoundary(currentX, currentY, currentZ);
							}
							break;  
						}
				}
			}
		} while(hitIt == false);


		int l = whichBoundary(currentX, currentY, currentZ);

		//keep a moving average
		double a = (k*average)/(k+1);
		double b = 1.000*l/(k+1);
		average = a + b;
		//average = (k*average)/(k+1) + (double)(1/(k+1))*l;
	}

	return average;
}

int main()
{
	srand(time(0));
	double result[GRID_X_DIMENSION][GRID_Y_DIMENSION][GRID_Z_DIMENSION];

	//initialize array
	// can juse use int myArray[size][size][size] = {0};
	for(int i = 0; i < GRID_X_DIMENSION; i++)
	{
		for(int j = 0; j < GRID_Y_DIMENSION; j++)
		{
			for(int k = 0; k < GRID_Z_DIMENSION; k++)
			{
				result[i][j][k] = 0.0;    
			}
		}
	}

	//Start with walkers at each non-boundary point  equal to the MULTIPLICITY

	double iterations = 0.0;
	double x_val = static_cast<double>(GRID_X_DIMENSION);
	double y_val = static_cast<double>(GRID_Y_DIMENSION);
	double z_val = static_cast<double>(GRID_Z_DIMENSION);
	double TOTAL_ITERATIONS = x_val*y_val*z_val;

	for(int i = 0; i < GRID_X_DIMENSION; i++)
	{
		for(int j = 0; j < GRID_Y_DIMENSION; j++)
		{
			for(int k = 0; k < GRID_Z_DIMENSION; k++)
			{
				result[i][j][k] = walker(i,j,k);    
				iterations++;
				if(abs(fmod(iterations,100.0)) < 0.001)
				{
					std::cout << "Progress: " <<  std::setprecision(4) << iterations/(TOTAL_ITERATIONS)*100.0 << "%     \r" << std::flush;
				}
			}
		}
	}
	std::cout << "iterations: " << iterations << std::endl;

	ofstream resultFile;
	resultFile.open ("result.txt");
	for(int p = 0; p <= GRID_Z_DIMENSION-1; p++)
	{
		resultFile << "z = ";
		resultFile << p;
		resultFile << "\n";
		for(int m = (GRID_Y_DIMENSION-1); m >= 0; m--)
		{
			for(int n = 0; n <= GRID_X_DIMENSION-1; n++)
			{
				//resultFile << resultArray[i][j];
				resultFile << result[n][m][p];
				resultFile << ", ";
			}
			resultFile << "\n";
		}
		resultFile << "\n";
		resultFile << "\n";
	}
	resultFile.close();
	return 0;
}
