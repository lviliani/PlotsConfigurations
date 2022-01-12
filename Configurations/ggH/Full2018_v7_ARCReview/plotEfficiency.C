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

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_em/"+var+"/histo_ggH_hww");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_em/"+var+"/histo_ggH_hww");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_em/"+var+"/histo_ggH_hww");
  h_pass_DoubleMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleMu_em/"+var+"/histo_ggH_hww");
  h_pass_DoubleE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleE_em/"+var+"/histo_ggH_hww");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_em/"+var+"/histo_ggH_hww");

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
   //legend->AddEntry(graFormula,"Comb trigger formula","p");
   legend->Draw();

  c->Print("ggH_TriggerEff_Direct_em_"+var+"allflav.png");
  c->Clear();

   TH1F *hme_total;
   TH1F *hme_pass_singlEl;
   TH1F *hme_pass_singlMu;
   TH1F *hme_pass_ElMu;
   TH1F *hme_pass_DoubleMu;
   TH1F *hme_pass_DoubleE;
   TH1F *hme_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  hme_total = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww");
  hme_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_me/"+var+"/histo_ggH_hww");
  hme_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_me/"+var+"/histo_ggH_hww");
  hme_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_me/"+var+"/histo_ggH_hww");
  hme_pass_DoubleMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleMu_me/"+var+"/histo_ggH_hww");
  hme_pass_DoubleE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleE_me/"+var+"/histo_ggH_hww");
  hme_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_me/"+var+"/histo_ggH_hww");

  TMultiGraph *mgme = new TMultiGraph();
  TGraphAsymmErrors *grame_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors();

  grame_singlEl = new TGraphAsymmErrors (hme_pass_singlEl,hme_total);
  grame_singlMu = new TGraphAsymmErrors (hme_pass_singlMu,hme_total);
  grame_ElMu = new TGraphAsymmErrors (hme_pass_ElMu,hme_total);
  grame_DoubleMu = new TGraphAsymmErrors (hme_pass_DoubleMu,hme_total);
  grame_DoubleE = new TGraphAsymmErrors (hme_pass_DoubleE,hme_total);
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
  mgme->Add(grame_DoubleMu);
  mgme->Add(grame_DoubleE);
  mgme->Add(grame_Trig);
  //mgme->Add(grameFormula);

  grame_singlEl->SetLineColor(1);
  grame_singlMu->SetLineColor(2);
  grame_ElMu->SetLineColor(3);
  grame_DoubleMu->SetLineColor(5);
  grame_DoubleE->SetLineColor(7);
  grame_Trig->SetLineColor(4);
  grameFormula->SetLineColor(6);

  grame_singlEl->SetMarkerStyle(20);
  grame_singlMu->SetMarkerStyle(20);
  grame_ElMu->SetMarkerStyle(20);
  grame_DoubleMu->SetMarkerStyle(20);
  grame_DoubleE->SetMarkerStyle(20);
  grame_Trig->SetMarkerStyle(20);
  grameFormula->SetMarkerStyle(20);

  grame_singlEl->SetMarkerColor(1);
  grame_singlMu->SetMarkerColor(2);
  grame_ElMu->SetMarkerColor(3);
  grame_DoubleMu->SetMarkerColor(5);
  grame_DoubleE->SetMarkerColor(7);
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
   legendme->AddEntry(gra_DoubleMu,"DoubleMu","p");
   legendme->AddEntry(gra_DoubleE,"DoubleE","p");
   legendme->AddEntry(gra_Trig,"Comb","p");
   //legendme->AddEntry(grameFormula,"Comb trigger formula","p");
   legendme->Draw();

  cme->Print("ggH_TriggerEff_Direct_me_"+var+"allflav.png");
  cme->Clear();





   TH1F *hmm_total;
   TH1F *hmm_pass_singlEl;
   TH1F *hmm_pass_singlMu;
   TH1F *hmm_pass_ElMu;
   TH1F *hmm_pass_DoubleMu;
   TH1F *hmm_pass_DoubleE;
   TH1F *hmm_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  hmm_total = (TH1F*)f->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww");
  hmm_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_mm/"+var+"/histo_ggH_hww");
  hmm_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_mm/"+var+"/histo_ggH_hww");
  hmm_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_mm/"+var+"/histo_ggH_hww");
  hmm_pass_DoubleMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleMu_mm/"+var+"/histo_ggH_hww");
  hmm_pass_DoubleE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleE_mm/"+var+"/histo_ggH_hww");
  hmm_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_mm/"+var+"/histo_ggH_hww");

  TMultiGraph *mgmm = new TMultiGraph();
  TGraphAsymmErrors *gramm_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_Trig = new TGraphAsymmErrors();

  gramm_singlEl = new TGraphAsymmErrors (hmm_pass_singlEl,hmm_total);
  gramm_singlMu = new TGraphAsymmErrors (hmm_pass_singlMu,hmm_total);
  gramm_ElMu = new TGraphAsymmErrors (hmm_pass_ElMu,hmm_total);
  gramm_DoubleMu = new TGraphAsymmErrors (hmm_pass_DoubleMu,hmm_total);
  gramm_DoubleE = new TGraphAsymmErrors (hmm_pass_DoubleE,hmm_total);
  gramm_Trig = new TGraphAsymmErrors (hmm_pass_Trig,hmm_total);

  TGraph *grammFormula = new TGraph();

  for (int i=0; i<gramm_ElMu->GetN(); ++i){
    double xse,yse,xsm,ysm,xd,yd;
    gramm_singlEl->GetPoint(i,xse,yse);
    gramm_singlMu->GetPoint(i,xsm,ysm);
    gramm_ElMu->GetPoint(i,xd,yd);
    double eff_sing = yse + ysm - yse*ysm;
    double eff_dbl = yd;
    double eff_evt = eff_sing + eff_dbl - eff_sing*eff_dbl;
    grammFormula->SetPoint(i,xd,eff_evt);
  }


  mgmm->Add(gramm_singlEl);
  mgmm->Add(gramm_singlMu);
  mgmm->Add(gramm_ElMu);
  mgmm->Add(gramm_DoubleMu);
  mgmm->Add(gramm_DoubleE);
  mgmm->Add(gramm_Trig);
  //mgmm->Add(grammFormula);

  gramm_singlEl->SetLineColor(1);
  gramm_singlMu->SetLineColor(2);
  gramm_ElMu->SetLineColor(3);
  gramm_DoubleMu->SetLineColor(5);
  gramm_DoubleE->SetLineColor(7);
  gramm_Trig->SetLineColor(4);
  grammFormula->SetLineColor(6);

  gramm_singlEl->SetMarkerStyle(20);
  gramm_singlMu->SetMarkerStyle(20);
  gramm_ElMu->SetMarkerStyle(20);
  gramm_DoubleMu->SetMarkerStyle(20);
  gramm_DoubleE->SetMarkerStyle(20);
  gramm_Trig->SetMarkerStyle(20);
  grammFormula->SetMarkerStyle(20);

  gramm_singlEl->SetMarkerColor(1);
  gramm_singlMu->SetMarkerColor(2);
  gramm_ElMu->SetMarkerColor(3);
  gramm_DoubleMu->SetMarkerColor(5);
  gramm_DoubleE->SetMarkerColor(7);
  gramm_Trig->SetMarkerColor(4);
  grammFormula->SetMarkerColor(6);

  mgmm->SetTitle(hmm_total->GetTitle());
  TCanvas *cmm = new TCanvas("cmm","",200,10,600,500);

  mgmm->Draw("APE");
  mgmm->SetMinimum(0.0);
  mgmm->SetMaximum(1.015);
  mgmm->GetXaxis()->SetTitle(var);
  mgmm->GetXaxis()->CenterTitle(1);
  mgmm->GetXaxis()->SetTitleOffset(1.2);
  mgmm->GetYaxis()->SetTitle("Trig Eff");
  mgmm->GetYaxis()->CenterTitle(1);
  mgmm->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legendmm = new TLegend(0.5,0.1,0.8,0.3);
   legendmm->AddEntry(gra_singlEl,"SingleEle","p");
   legendmm->AddEntry(gra_singlMu,"SingleMu","p");
   legendmm->AddEntry(gra_ElMu,"E+Mu","p");
   legendmm->AddEntry(gra_DoubleMu,"DoubleMu","p");
   legendmm->AddEntry(gra_DoubleE,"DoubleE","p");
   legendmm->AddEntry(gra_Trig,"Comb","p");
   //legendmm->AddEntry(grammFormula,"Comb trigger formula","p");
   legendmm->Draw();

  cmm->Print("ggH_TriggerEff_Direct_mm_"+var+"allflav.png");
  cmm->Clear();


   TH1F *hee_total;
   TH1F *hee_pass_singlEl;
   TH1F *hee_pass_singlMu;
   TH1F *hee_pass_ElMu;
   TH1F *hee_pass_DoubleMu;
   TH1F *hee_pass_DoubleE;
   TH1F *hee_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  hee_total = (TH1F*)f->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww");
  hee_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_ee/"+var+"/histo_ggH_hww");
  hee_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_ee/"+var+"/histo_ggH_hww");
  hee_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_ee/"+var+"/histo_ggH_hww");
  hee_pass_DoubleMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleMu_ee/"+var+"/histo_ggH_hww");
  hee_pass_DoubleE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleE_ee/"+var+"/histo_ggH_hww");
  hee_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ee/"+var+"/histo_ggH_hww");

  TMultiGraph *mgee = new TMultiGraph();
  TGraphAsymmErrors *graee_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_Trig = new TGraphAsymmErrors();

  graee_singlEl = new TGraphAsymmErrors (hee_pass_singlEl,hee_total);
  graee_singlMu = new TGraphAsymmErrors (hee_pass_singlMu,hee_total);
  graee_ElMu = new TGraphAsymmErrors (hee_pass_ElMu,hee_total);
  graee_DoubleMu = new TGraphAsymmErrors (hee_pass_DoubleMu,hee_total);
  graee_DoubleE = new TGraphAsymmErrors (hee_pass_DoubleE,hee_total);
  graee_Trig = new TGraphAsymmErrors (hee_pass_Trig,hee_total);

  TGraph *graeeFormula = new TGraph();

  for (int i=0; i<graee_ElMu->GetN(); ++i){
    double xse,yse,xsm,ysm,xd,yd;
    graee_singlEl->GetPoint(i,xse,yse);
    graee_singlMu->GetPoint(i,xsm,ysm);
    graee_ElMu->GetPoint(i,xd,yd);
    double eff_sing = yse + ysm - yse*ysm;
    double eff_dbl = yd;
    double eff_evt = eff_sing + eff_dbl - eff_sing*eff_dbl;
    graeeFormula->SetPoint(i,xd,eff_evt);
  }


  mgee->Add(graee_singlEl);
  mgee->Add(graee_singlMu);
  mgee->Add(graee_ElMu);
  mgee->Add(graee_DoubleMu);
  mgee->Add(graee_DoubleE);
  mgee->Add(graee_Trig);
  //mgee->Add(graeeFormula);

  graee_singlEl->SetLineColor(1);
  graee_singlMu->SetLineColor(2);
  graee_ElMu->SetLineColor(3);
  graee_DoubleMu->SetLineColor(5);
  graee_DoubleE->SetLineColor(7);
  graee_Trig->SetLineColor(4);
  graeeFormula->SetLineColor(6);

  graee_singlEl->SetMarkerStyle(20);
  graee_singlMu->SetMarkerStyle(20);
  graee_ElMu->SetMarkerStyle(20);
  graee_DoubleMu->SetMarkerStyle(20);
  graee_DoubleE->SetMarkerStyle(20);
  graee_Trig->SetMarkerStyle(20);
  graeeFormula->SetMarkerStyle(20);

  graee_singlEl->SetMarkerColor(1);
  graee_singlMu->SetMarkerColor(2);
  graee_ElMu->SetMarkerColor(3);
  graee_DoubleMu->SetMarkerColor(5);
  graee_DoubleE->SetMarkerColor(7);
  graee_Trig->SetMarkerColor(4);
  graeeFormula->SetMarkerColor(6);

  mgee->SetTitle(hee_total->GetTitle());
  TCanvas *cee = new TCanvas("cee","",200,10,600,500);

  mgee->Draw("APE");
  mgee->SetMinimum(0.0);
  mgee->SetMaximum(1.015);
  mgee->GetXaxis()->SetTitle(var);
  mgee->GetXaxis()->CenterTitle(1);
  mgee->GetXaxis()->SetTitleOffset(1.2);
  mgee->GetYaxis()->SetTitle("Trig Eff");
  mgee->GetYaxis()->CenterTitle(1);
  mgee->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legendee = new TLegend(0.5,0.1,0.8,0.3);
   legendee->AddEntry(gra_singlEl,"SingleEle","p");
   legendee->AddEntry(gra_singlMu,"SingleMu","p");
   legendee->AddEntry(gra_ElMu,"E+Mu","p");
   legendee->AddEntry(gra_DoubleMu,"DoubleMu","p");
   legendee->AddEntry(gra_DoubleE,"DoubleE","p");
   legendee->AddEntry(gra_Trig,"Comb","p");
   //legendee->AddEntry(graeeFormula,"Comb trigger formula","p");
   legendee->Draw();

  cee->Print("ggH_TriggerEff_Direct_ee_"+var+"allflav.png");
  cee->Clear();



}// end of program
