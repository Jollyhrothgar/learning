#include<iostream>
using namespace std;
void set_content_BINS()
{
	TH1F* h1 = new TH1F("h1","Set Bins",10,0,5);
	TH1F* h2 = new TH1F("h2","Set Bins",10,0,5);
	h1->SetLineColor(3);
	h2->SetLineColor(4);
	TCanvas* c2 = new TCanvas("c2","Set Bins");

	for(int i = 0; i < 10; i++)
	{
		// All bins are accessed by the bin index.
		// This routine will pick a bin, accessed by its index
		// and set that bin to the value i*0.2
		h1->SetBinContent(i,i*0.2);
		h2->SetBinContent(i,i*0.2);
	}
	
	// Fill works differently. Fill will increase a bin's value by one
	// if no weight is specified. If weight is specified, then Fill will
	// increase that bin's value by the weight given. In this case, one
	// may have wished to fill the third bin with the number 1. In actuality
	// what is happening is that the histogram bin containing the number '3'
	// will be increased in value by 1.
	h1->Fill(3,1);
	h1->Draw();
	h2->Draw("same");
}
