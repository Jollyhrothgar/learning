// Design Goal: this class file will store different objects that will allow
// for an N-body gravitational simulation. This class file should store all
// neccessary functions, objects, etc to perform the simulation.
//
// Star Class:
// 1. Store position, mass, and velocity of a star.
// 2. Store the total net force acting on it.
// 3. Optional extra feature: keep a list of spectral types in main sequence,
//    and identify spectral type by input mass. Could also do with radius, luminosity
//    etc...
//
// F_Star Class:
// 1. Take two star objects, find the net force between the two stars,
//    update each Star's total net force. This function would take two stars
//    and find the gravitational force between them. Then, the function would
//    automatically add the previous stored force, and the new force together
//    as vectors. Upon looping through a set of stars, we would arrive at the
//    total net force on each star, and could run through a time step.
//
// Move_Star Class:
// 1. This class would be used to update the position of each star, using
//    a given time step. You would input the star, and the desired time step,
//    and then, this class would use the star's stored net force to calculate
//    the accelleration of the star, and find its new position and velocity. 
// 

// Now, we must write down the class definition of the star, (ensuring all functions we use are
// in the namespace of star...

// Define constructor
#include "Galaxy.h"

star::star(double m, double x, double y, double z, double xvel, double yvel, double zvel, double fx, double fy, double fz)
{
	mass = m;
	x_pos = x;
	y_pos = y;
	z_pos = z;
	vx = xvel;
	vy = yvel;
	vz = zvel;
	fx_net = fx;
	fy_net = fy;
	fz_net = fz;
}

star::~star(void)
{
}
// Define Member Functions - Input
double star::GetX()
{
	return x_pos;
}

double star::GetY()
{
	return y_pos;
}

double star::GetZ()
{
	return z_pos;
}

double star::GetMass(void)
{
	return mass;
}

double star::GetVX(void)
{
	return vx;
}

double star::GetVY(void)
{
	return vy;
}

double star::GetVZ(void)
{
	return vz;
}

double star::GetFXnet()
{
	return fx_net;
}

double star::GetFYnet()
{
	return fy_net;
}

double star::GetFZnet()
{
	return fz_net;
}

void CForce(star &temp1, star &temp2)
{
	*temp1.mass = *temp2.mass;
}
