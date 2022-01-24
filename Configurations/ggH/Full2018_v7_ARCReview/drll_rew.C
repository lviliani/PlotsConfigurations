void drll_rew(TString flav="em", TString sample = "ggH_hww"){

TString var = "drll";
TString dir = "rootFileV2_drll";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7.root");

TString dir2 = "Eff_fromTnP/rootFile_drll";

TFile *f2 = TFile::Open(dir2+"/plots_ggH2018_v7_TnPEff.root");

  TH1F *h_total;
  TH1F *h_pass_Trig;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_"+sample);
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_"+flav+"/"+var+"/histo_"+sample);

  TH1F *hTP_total;
  TH1F *hTP_pass_Trig;
  TH1F *hTP_pass_TrigUp;
  TH1F *hTP_pass_TrigDown;

  hTP_total = (TH1F*)f2->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_"+sample);
  hTP_pass_Trig = (TH1F*)f2->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_"+sample+"_Trig");

  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors (h_pass_Trig, h_total);

  TGraphAsymmErrors *graTPme_Trig = new TGraphAsymmErrors (hTP_pass_Trig, hTP_total);

   TString weight_func = "(";
   for (int i=0; i<grame_Trig->GetN(); ++i){
    double x,y,xtp,ytp;
    grame_Trig->GetPoint(i,x,y);
    graTPme_Trig->GetPoint(i,xtp,ytp);
    cout << x << endl; 
    if (x==0.125) weight_func += "(drll >= "+to_string(x-0.125)+" && drll <"+to_string(x+0.125)+")*"+to_string(y/ytp)+" + ";
    else if (x==0.375) weight_func += "(drll >= "+to_string(x-0.125)+" && drll <"+to_string(x+0.125)+")*"+to_string(y/ytp)+" + ";
    else weight_func += "(drll >= "+to_string(x-0.25)+" && drll <"+to_string(x+0.25)+")*"+to_string(y/ytp)+" + ";
    cout << flav << " DRll = " <<  x << " "  << y/ytp << endl; 
  }
  weight_func += ")";

  cout << weight_func << endl;

}
