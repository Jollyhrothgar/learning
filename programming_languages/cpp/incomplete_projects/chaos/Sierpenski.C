#include <iostream>
#include <vector>

// ROOT
#include "TCanvas.h"
#include "TGraph.h"
#include "TH1F.h"
#include "TRandom.h"



const double PI = 3.1415926535897931;

void   midway_point(double &mx, double &my, double ux, double uy, double vx, double vy);

int Sierpenski(int stop_value = 30000)
{
	TCanvas* view = new TCanvas("view","View Chaos Game", 800, 800);
	TGraph* set = new TGraph();
	set->SetName("Sierpenski Points");
	set->SetTitle("Sierpenski ");
	set->SetMarkerStyle(6);
	TGraph* gFrame = new TGraph();
	gFrame->SetPoint(0,0.0,0.0);
	gFrame->SetPoint(1,1.0,1.0);

	view->Update();

	set->Draw("AP");

	TRandom* val = new TRandom();

	// Seed triangle
	double v0_x = 0.0;
	double v0_y = 0.0;
	double v1_x = 1.0;
	double v1_y = 0.0;
	double v2_x = cos(60.0*PI/180.0);
	double v2_y = sin(60.0*PI/180.0);
	
	std::cout << "Triangle: (" << v0_x << ", " << v0_y << "), (" << v1_x << ", " << v1_y << "), (" << v2_x << ", " << v2_y << ")" << std::endl;

	double x_rand = 0.5;
	double y_rand = 0.5;

	std::cout << "Starting from (" << x_rand << ", " << y_rand << ")" << std::endl;
	// generate random vertex 0 - v0, 1 - v1, 2 - v2
	int i = 0;
	for(i = 0; i < stop_value; i++)
	{
		int vertex = val->Integer(3);

		// move plot point halfway between x_rand, y_rand and vertex.
		double mpx;
		double mpy;

		double mpx0;
		double mpy0;

		if( i == 1 )
		{
			switch(vertex)
			{
				case 0:
					midway_point(mpx,mpy,x_rand,y_rand,v0_x,v0_y);	
					break;
				case 1:
					midway_point(mpx,mpy,x_rand,y_rand,v1_x,v1_y);	
					break;
				case 2:
					midway_point(mpx,mpy,x_rand,y_rand,v2_x,v2_y);	
					break;
				default:
					std::cout << "BLOODY FUCKING MURDER ROOT GOT BROKE!!!" << std::endl;
			}
		}
		else
		{
			switch(vertex)
			{
				case 0:
					midway_point(mpx0,mpy0,mpx,mpy,v0_x,v0_y);	
					break;
				case 1:
					midway_point(mpx0,mpy0,mpx,mpy,v1_x,v1_y);	
					break;
				case 2:
					midway_point(mpx0,mpy0,mpx,mpy,v2_x,v2_y);	
					break;
				default:
					std::cout << "BLOODY FUCKING MURDER ROOT GOT BROKE!!!" << std::endl;
			}
			mpx = mpx0;
			mpy = mpy0;
		}
		if(mpx < 0.0 || mpy < 0.0)
		{
			std::cout << i << std::endl;
			continue;
		}
		set->SetPoint(set->GetN(), mpx, mpy);
		if(i%1000 == 0) view->Update();
	}

	return 0;
}

// gives mx and my the values of the midpoint between vectors u and v
void midway_point(double &mx, double &my, double ux, double uy, double vx, double vy)
{
	mx = (ux + vx)*0.5;
	my = (uy + vy)*0.5;
}
