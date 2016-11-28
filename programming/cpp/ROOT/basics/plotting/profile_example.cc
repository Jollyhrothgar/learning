#include "profile_example.h"

void profile_example()
{
	TCanvas* c1 = new TCanvas("c1","Profile histogram example",200,10,700,500);
	TCanvas* c2 = new TCanvas("c2","2D histogram example",200,10,700,500);
	TCanvas* c3 = new TCanvas("c3","TGraph Test",200,10,700,500);
	TCanvas* c4 = new TCanvas("c4","TGraph Test2", 200,10,700,500);
	TProfile * hprof  = new TProfile("hprof","Profile of pz versus px",100,-4,4,0,20);
	TH2F * hist2D = new TH2F("2dhist","Plot of pz vs px and py",100,-4,4,100,-4,4);
	vector<float> vpx(25000,0.0); // initialize a different TGraph using the vector
	vector<float> vpy(25000,0.0);
	vector<float> vpz(25000,0.0);

	TGraph2D* test1 = new TGraph2D(25000); // intitalized with total number of expected points
	test1->SetName("test1");
	test1->SetTitle("Filled over Loop;px;py;pz"); // Title string parsed: title;xaxiz;yaxis;zaxis
	float px, py, pz;
	for ( int i=0; i<25000; i++) 
	{
		gRandom->Rannor(px,py);
		pz = px*px + py*py;
		hprof->Fill(px,pz,1);
		hist2D->Fill(px,py,pz); 
		vpx[i] = px;
		vpy[i] = py;
		vpz[i] = pz; 
		test1->SetPoint(i,px,py,pz);
	}
	TGraph2D* test2 = new TGraph2D(vpx.size(),&vpx[0],&vpy[0],&vpz[0]);
	test2->SetTitle("Filled with vectors;px;py;pz"); // Title string parsed: title;xaxiz;yaxis;zaxis
	test2->SetName("test2");
	c1->cd();
	hprof->Draw();
	c2->cd();
	hist2D->Draw("SURF2z"); // surf1 is a surface style, which overlays color on a simple
							// conntected grid, the z option automatically creates a color
							// palette.
	c3->cd();
	test1->SetMarkerStyle(kFullCircle);
	test1->Draw("APcolz");
	c4->cd();
	test2->SetMarkerStyle(kFullCircle);
	test2->Draw("AP");
}
