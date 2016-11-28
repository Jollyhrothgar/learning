void one_to_one_BINS()
{
	TH1I * h1 = new TH1I("h1","bin-test",10,1,10);
	TCanvas * c1 = new TCanvas("c1","bin-test-canvas");
	for(int i = 1; i<11; i++)
	{
		h1->Fill(i,i);
	}
	h1->Draw();
	for(int i = 0; i<12; i++)
	{
		cout << "h1 bin: " << i << " is: " << h1->GetBinContent(i) << endl;
	}
}
