#include "Galaxy.C"
#include<iostream>
using namespace std;

int main()
{
	// Sun(m,x,y,z,vx,vy,vz,fx,fy,fz)
	star Sun(1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0);
	cout << Sun.GetMass() << endl;
	cout << Sun.GetX() << endl;
	cout << Sun.GetY() << endl;
	cout << Sun.GetZ() << endl;
	cout << Sun.GetVX() << endl;
	cout << Sun.GetVY() << endl;
	cout << Sun.GetVZ() << endl;
	cout << Sun.GetFXnet() << endl;
	cout << Sun.GetFYnet() << endl;
	cout << Sun.GetFZnet() << endl;
	
	star Moon(0,0,0,0,0,0,0,0,0,0);
	CForce(Moon,Sun);
	
	cout << Sun.GetMass() << endl;
	cout << Moon.GetMass() << endl;
	return 0;
}
