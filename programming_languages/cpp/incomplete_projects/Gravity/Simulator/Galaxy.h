class star
{
	public:
		//Constructor
		star(double m, double x, double y, double z, double xvel, double yvel, double zvel, double fx, double fy, double fz);
		//Destructor
		~star(void);
		
		//Output
		double GetMass();
		double GetX();
		double GetY();
		double GetZ();

		double GetVX();
		double GetVY();
		double GetVZ();
		double GetFXnet();
		double GetFYnet();
		double GetFZnet();
		// Note that position, velocity, and force will be updated by Kinematics.
	friend void CForce(star &temp1, star &temp2);	
	
	protected:
		double  mass, x_pos, y_pos, z_pos, vx, vy, vz, fx_net, fy_net, fz_net;
};
