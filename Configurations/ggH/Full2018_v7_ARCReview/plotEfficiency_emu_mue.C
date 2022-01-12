void plotEfficiency_emu_mue(TString var="eta1"){ 

TString dir = "rootFile_mue_emu";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7.root");

   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_MuE;
   TH1F *h_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_em/"+var+"/histo_ggH_hww");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_em/"+var+"/histo_ggH_hww");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_em/"+var+"/histo_ggH_hww");
  h_pass_MuE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_MuE_em/"+var+"/histo_ggH_hww");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_em/"+var+"/histo_ggH_hww");

  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_MuE = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();

//  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
//  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);



  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);
  gra_ElMu = new TGraphAsymmErrors (h_pass_ElMu,h_total);
  gra_MuE = new TGraphAsymmErrors (h_pass_MuE,h_total);
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
  mg->Add(gra_MuE);
  mg->Add(gra_Trig);
//  mg->Add(graFormula);

  gra_singlEl->SetLineColor(1);
  gra_singlMu->SetLineColor(2);
  gra_ElMu->SetLineColor(3);
  gra_MuE->SetLineColor(5);
  gra_Trig->SetLineColor(4);
  graFormula->SetLineColor(6);

  gra_singlEl->SetMarkerStyle(20);
  gra_singlMu->SetMarkerStyle(20);
  gra_ElMu->SetMarkerStyle(20);
  gra_MuE->SetMarkerStyle(20);

  gra_Trig->SetMarkerStyle(20);
  graFormula->SetMarkerStyle(20);

  gra_singlEl->SetMarkerColor(1);
  gra_singlMu->SetMarkerColor(2);
  gra_ElMu->SetMarkerColor(3);
  gra_MuE->SetMarkerColor(5);
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
   legend->AddEntry(gra_MuE,"Mu+E","p");
   legend->AddEntry(gra_Trig,"Comb","p");
   legend->AddEntry(graFormula,"Comb trigger formula","p");
   legend->Draw();

  c->Print("ggH_TriggerEff_Direct_em_"+var+"emu_mue.png");
  c->Clear();

   TH1F *hme_total;
   TH1F *hme_pass_singlEl;
   TH1F *hme_pass_singlMu;
   TH1F *hme_pass_ElMu;
   TH1F *hme_pass_MuE;
   TH1F *hme_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  hme_total = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww");
  hme_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_me/"+var+"/histo_ggH_hww");
  hme_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_me/"+var+"/histo_ggH_hww");
  hme_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_me/"+var+"/histo_ggH_hww");
  hme_pass_MuE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_MuE_me/"+var+"/histo_ggH_hww");
  hme_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_me/"+var+"/histo_ggH_hww");

  TMultiGraph *mgme = new TMultiGraph();
  TGraphAsymmErrors *grame_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_MuE = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors();

  grame_singlEl = new TGraphAsymmErrors (hme_pass_singlEl,hme_total);
  grame_singlMu = new TGraphAsymmErrors (hme_pass_singlMu,hme_total);
  grame_ElMu = new TGraphAsymmErrors (hme_pass_ElMu,hme_total);
  grame_MuE = new TGraphAsymmErrors (hme_pass_MuE,hme_total);
  grame_Trig = new TGraphAsymmErrors (hme_pass_Trig,hme_total);

  TGraph *grameFormula = new TGraph();

  for (int i=0; i<grame_ElMu->GetN(); ++i){
    double xse,yse,xsm,ysm,xd,yd;
    grame_singlEl->GetPoint(i,xse,yse);
    grame_singlMu->GetPoint(i,xsm,ysm);
    grame_ElMu->GetPoint(i,xd,yd);
    double eff_sing = yse + ysm - yse*ysm;
    double eff_dbl = yd;
    double eff_evt = eff_sing + eff_dbl - eff_sing*eff_dbl;
    grameFormula->SetPoint(i,xd,eff_evt);
  }


  mgme->Add(grame_singlEl);
  mgme->Add(grame_singlMu);
  mgme->Add(grame_ElMu);
  mgme->Add(grame_MuE);
  mgme->Add(grame_Trig);
//  mgme->Add(grameFormula);

  grame_singlEl->SetLineColor(1);
  grame_singlMu->SetLineColor(2);
  grame_ElMu->SetLineColor(3);
  grame_MuE->SetLineColor(5);
  grame_Trig->SetLineColor(4);
  grameFormula->SetLineColor(6);

  grame_singlEl->SetMarkerStyle(20);
  grame_singlMu->SetMarkerStyle(20);
  grame_ElMu->SetMarkerStyle(20);
  grame_MuE->SetMarkerStyle(20);
  grame_Trig->SetMarkerStyle(20);
  grameFormula->SetMarkerStyle(20);

  grame_singlEl->SetMarkerColor(1);
  grame_singlMu->SetMarkerColor(2);
  grame_ElMu->SetMarkerColor(3);
  grame_MuE->SetMarkerColor(5);
  grame_Trig->SetMarkerColor(4);
  grameFormula->SetMarkerColor(6);

  mgme->SetTitle(hme_total->GetTitle());
  TCanvas *cme = new TCanvas("cme","",200,10,600,500);

  mgme->Draw("APE");
  mgme->SetMinimum(0.0);
  mgme->SetMaximum(1.015);
  mgme->GetXaxis()->SetTitle(var);
  mgme->GetXaxis()->CenterTitle(1);
  mgme->GetXaxis()->SetTitleOffset(1.2);
  mgme->GetYaxis()->SetTitle("Trig Eff");
  mgme->GetYaxis()->CenterTitle(1);
  mgme->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legendme = new TLegend(0.5,0.1,0.8,0.3);
   legendme->AddEntry(gra_singlEl,"SingleEle","p");
   legendme->AddEntry(gra_singlMu,"SingleMu","p");
   legendme->AddEntry(gra_ElMu,"E+Mu","p");
   legendme->AddEntry(gra_MuE,"Mu+E","p");
   legendme->AddEntry(gra_Trig,"Comb","p");
   legendme->AddEntry(grameFormula,"Comb trigger formula","p");
   legendme->Draw();

  cme->Print("ggH_TriggerEff_Direct_me_"+var+"emu_mue.png");
  cme->Clear();



}// end of program
