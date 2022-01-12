void plotEfficiency(TString var="eta1"){ 

TString dir = "rootFile_allflav";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7.root");

   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_DoubleMu;
   TH1F *h_pass_DoubleE;
   TH1F *h_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV/"+var+"/histo_WH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl/"+var+"/histo_WH_hww");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu/"+var+"/histo_WH_hww");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu/"+var+"/histo_WH_hww");
  h_pass_DoubleMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleMu/"+var+"/histo_WH_hww");
  h_pass_DoubleE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleE/"+var+"/histo_WH_hww");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig/"+var+"/histo_WH_hww");

  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();


  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);
  gra_ElMu = new TGraphAsymmErrors (h_pass_ElMu,h_total);
  gra_DoubleMu = new TGraphAsymmErrors (h_pass_DoubleMu,h_total);
  gra_DoubleE = new TGraphAsymmErrors (h_pass_DoubleE,h_total);
  gra_Trig = new TGraphAsymmErrors (h_pass_Trig,h_total);
   
  TGraph *graFormula = new TGraph();

  for (int i=0; i<gra_ElMu->GetN(); ++i){
    double xse,yse,xsm,ysm,xd,yd;
    gra_singlEl->GetPoint(i,xse,yse);
    gra_singlMu->GetPoint(i,xsm,ysm);
    gra_ElMu->GetPoint(i,xd,yd);
    double eff_sing = yse + ysm - yse*ysm;
    double eff_dbl = yd;
    double eff_evt = eff_sing + eff_dbl - eff_sing*eff_dbl;
    graFormula->SetPoint(i,xd,eff_evt);
  }

  mg->Add(gra_singlEl);
  mg->Add(gra_singlMu);
  mg->Add(gra_ElMu);
  mg->Add(gra_DoubleMu);
  mg->Add(gra_DoubleE);
  mg->Add(gra_Trig);
  //mg->Add(graFormula);

  gra_singlEl->SetLineColor(1);
  gra_singlMu->SetLineColor(2);
  gra_ElMu->SetLineColor(3);
  gra_DoubleMu->SetLineColor(5);
  gra_DoubleE->SetLineColor(7);
  gra_Trig->SetLineColor(4);
  graFormula->SetLineColor(6);

  gra_singlEl->SetMarkerStyle(20);
  gra_singlMu->SetMarkerStyle(20);
  gra_ElMu->SetMarkerStyle(20);
  gra_DoubleMu->SetMarkerStyle(20);
  gra_DoubleE->SetMarkerStyle(20);
  gra_Trig->SetMarkerStyle(20);
  graFormula->SetMarkerStyle(20);

  gra_singlEl->SetMarkerColor(1);
  gra_singlMu->SetMarkerColor(2);
  gra_ElMu->SetMarkerColor(3);
  gra_DoubleMu->SetMarkerColor(5);
  gra_DoubleE->SetMarkerColor(7);
  gra_Trig->SetMarkerColor(4);
  graFormula->SetMarkerColor(6);

  mg->SetTitle(h_total->GetTitle());
  TCanvas *c = new TCanvas("c","",200,10,600,500);

  mg->Draw("APE");
  mg->SetMinimum(0.0);
  mg->SetMaximum(1.015);
  mg->GetXaxis()->SetTitle(var);
  mg->GetXaxis()->CenterTitle(1);
  mg->GetXaxis()->SetTitleOffset(1.2);
  mg->GetYaxis()->SetTitle("Trig Eff");
  mg->GetYaxis()->CenterTitle(1);
  mg->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legend = new TLegend(0.5,0.1,0.8,0.3);
   legend->AddEntry(gra_singlEl,"SingleEle","p");
   legend->AddEntry(gra_singlMu,"SingleMu","p");
   legend->AddEntry(gra_ElMu,"E+Mu","p");
   legend->AddEntry(gra_DoubleMu,"DoubleMu","p");
   legend->AddEntry(gra_DoubleE,"DoubleE","p");
   legend->AddEntry(gra_Trig,"Comb","p");
   legend->AddEntry(graFormula,"Comb trigger formula","p");
   legend->Draw();

  c->Print("ggH_TriggerEff_Direct_"+var+".png");
  c->Clear();


}// end of program
