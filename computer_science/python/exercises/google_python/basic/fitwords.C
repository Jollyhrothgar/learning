#include<cmath>
fitwords(){
  std::ifstream in_file("bible_words_count.txt");
  double rank_num,count_num;
  TGraph* g = new TGraph();
  g->SetTitle("Zipf;rank;count");
  g->SetName("zipf");
  while(in_file>>rank_num>>count_num){
    g->SetPoint(g->GetN(), log(rank_num), log(count_num));
  }
  TF1* f = new TF1("fit","pol1",1.,305.);
  g->Fit(f,"R");
  g->Draw("ALP");
}
