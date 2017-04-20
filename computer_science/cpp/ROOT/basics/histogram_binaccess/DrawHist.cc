#include <iostream>

#include "TCanvas.h"
#include "TH1.h"
#include <iostream>
#include "TRandom.h"

void DrawHist()
{
	TH1F* hist = new TH1F("hist","Random hist",100,0,100);
	float f = 0.5;
	for(int i = 1; i <= 100; i++)
	{
		hist->SetBinContent(i,f);
		f++;
	}

	// Binning: bin 0     INCLUDES x-low
	// Binning: bin nbins EXCLUDES x-high
	hist->Draw();

	int thebin = 0;
	double thebinval = 30.5;
	thebin = hist->GetXaxis()->FindBin(thebinval);
	// Example where the value is not on a bin-edge
	std::cout << "Checking bin number for the quantitiy thebinval: " << thebinval; 
	std::cout << " and the bin number containing this value, thebin =  " << thebin << std::endl;
	std::cout << "This histogram has: " << hist->GetNbinsX() << " Bins" << std::endl;
	std::cout << "The Low edge of thebin is: " << hist->GetBinLowEdge(thebin) << std::endl;
	std::cout << "The bin content of the bin containing " << thebinval << " is: "; 
	std::cout << hist->GetBinContent(thebin) << std::endl;
}
