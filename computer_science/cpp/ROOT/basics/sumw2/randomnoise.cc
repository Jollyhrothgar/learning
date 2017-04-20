#include "randomnoise.h"

void showmethenoise()
{
	TH1F* noise = new TH1F("noise","Random Noise",100,-3,3);
	float f1, f2;
	for(int i = 0; i < 10000; i++)
	{
		gRandom->Rannor(f1,f2);
		noise->Fill(f1);
		noise->Fill(f2);
	}
	// In this case, using "->Draw("e")" or noise->Sumw2() will draw
	// the points with error bars for the histogram.
	//noise->Sumw2();	
	noise->Draw();
}
