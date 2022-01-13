void plotEfficiency(TString var="eta1", bool isData=false){

TString dir = isData ? "rootFile_dataTP" : "rootFile_final";


TFile *f = TFile::Open(dir+"/plots_ggH2018_v7_TnPEff.root");
TFile *ffix = TFile::Open("rootFile_dataTP/plots_ggH2018_v7_TnPEff.root");


   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_DoubleMu;
   TH1F *h_pass_DoubleE;
   TH1F *h_pass_Trig;
   TH1F *h_pass_TrigFix;

  // TGraphAsymmErrors *gra_2018A=0;

  h_total = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_singlEl");
  h_pass_singlMu = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_singlMu");
  h_pass_ElMu = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_ElMu");
  h_pass_DoubleMu = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_dblMu");
  h_pass_DoubleE = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_dblEl");
  h_pass_Trig = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_Trig");
  h_pass_TrigFix = (TH1F*)ffix->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_Trig");


  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_TrigFix = new TGraphAsymmErrors();


  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total,"cp");
  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total,"cp");
  gra_ElMu = new TGraphAsymmErrors (h_pass_ElMu,h_total,"cp");
  gra_DoubleMu = new TGraphAsymmErrors (h_pass_DoubleMu,h_total,"cp");
  gra_DoubleE = new TGraphAsymmErrors (h_pass_DoubleE,h_total,"cp");
  //gra_Trig = new TGraphAsymmErrors (h_pass_Trig,h_total,"cp");
  gra_TrigFix = new TGraphAsymmErrors (h_pass_TrigFix,h_total,"cp");

   
  mg->Add(gra_singlEl);
  mg->Add(gra_singlMu);
  mg->Add(gra_ElMu);
  mg->Add(gra_DoubleMu);
  mg->Add(gra_DoubleE);
  //mg->Add(gra_Trig);
  mg->Add(gra_TrigFix);

  gra_singlEl->SetLineColor(1);
  gra_singlMu->SetLineColor(2);
  gra_ElMu->SetLineColor(3);
  gra_DoubleMu->SetLineColor(5);
  gra_DoubleE->SetLineColor(7);
  gra_Trig->SetLineColor(4);
  gra_TrigFix->SetLineColor(4);

  gra_singlEl->SetMarkerStyle(20);
  gra_singlMu->SetMarkerStyle(20);
  gra_ElMu->SetMarkerStyle(20);
  gra_DoubleMu->SetMarkerStyle(20);
  gra_DoubleE->SetMarkerStyle(20);
  gra_Trig->SetMarkerStyle(20);
  gra_TrigFix->SetMarkerStyle(20);

  gra_singlEl->SetMarkerColor(1);
  gra_singlMu->SetMarkerColor(2);
  gra_ElMu->SetMarkerColor(3);
  gra_DoubleMu->SetMarkerColor(5);
  gra_DoubleE->SetMarkerColor(7);
  gra_Trig->SetMarkerColor(4);
  gra_TrigFix->SetMarkerColor(4);

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
   //legend->AddEntry(gra_Trig,"Comb","p");
   legend->AddEntry(gra_TrigFix,"Comb new formula","p");
   legend->Draw();

  TString tag = isData ? "DATA" : "MC";

  c->SaveAs("ggH_TriggerEff_from"+tag+"TnP_"+var+"_em.png");

  c->Clear();



   TH1F *hme_total;
   TH1F *hme_pass_singlEl;
   TH1F *hme_pass_singlMu;
   TH1F *hme_pass_ElMu;
   TH1F *hme_pass_DoubleMu;
   TH1F *hme_pass_DoubleE;
   TH1F *hme_pass_Trig;
   TH1F *hme_pass_TrigFix;

  // TGraphAsymmErrors *gra_2018A=0;

  hme_total = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww");
  hme_pass_singlEl = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_singlEl");
  hme_pass_singlMu = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_singlMu");
  hme_pass_ElMu = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_ElMu");
  hme_pass_DoubleMu = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_dblMu");
  hme_pass_DoubleE = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_dblEl");
  hme_pass_Trig = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_Trig");
  hme_pass_TrigFix = (TH1F*)ffix->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_Trig");


  TMultiGraph *mgme = new TMultiGraph();
  TGraphAsymmErrors *grame_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_TrigFix = new TGraphAsymmErrors();


  grame_singlEl = new TGraphAsymmErrors (hme_pass_singlEl,hme_total,"cp");
  grame_singlMu = new TGraphAsymmErrors (hme_pass_singlMu,hme_total,"cp");
  grame_ElMu = new TGraphAsymmErrors (hme_pass_ElMu,hme_total,"cp");
  grame_DoubleMu = new TGraphAsymmErrors (hme_pass_DoubleMu,hme_total,"cp");
  grame_DoubleE = new TGraphAsymmErrors (hme_pass_DoubleE,hme_total,"cp");
  //grame_Trig = new TGraphAsymmErrors (hme_pass_Trig,hme_total,"cp");
  grame_TrigFix = new TGraphAsymmErrors (hme_pass_TrigFix,hme_total,"cp");


  mgme->Add(grame_singlEl);
  mgme->Add(grame_singlMu);
  mgme->Add(grame_ElMu);
  mgme->Add(grame_DoubleMu);
  mgme->Add(grame_DoubleE);
  //mgme->Add(grame_Trig);
  mgme->Add(grame_TrigFix);

  grame_singlEl->SetLineColor(1);
  grame_singlMu->SetLineColor(2);
  grame_ElMu->SetLineColor(3);
  grame_DoubleMu->SetLineColor(5);
  grame_DoubleE->SetLineColor(7);
  grame_Trig->SetLineColor(4);
  grame_TrigFix->SetLineColor(4);

  grame_singlEl->SetMarkerStyle(20);
  grame_singlMu->SetMarkerStyle(20);
  grame_ElMu->SetMarkerStyle(20);
  grame_DoubleMu->SetMarkerStyle(20);
  grame_DoubleE->SetMarkerStyle(20);
  grame_Trig->SetMarkerStyle(20);
  grame_TrigFix->SetMarkerStyle(20);

  grame_singlEl->SetMarkerColor(1);
  grame_singlMu->SetMarkerColor(2);
  grame_ElMu->SetMarkerColor(3);
  grame_DoubleMu->SetMarkerColor(5);
  grame_DoubleE->SetMarkerColor(7);
  grame_Trig->SetMarkerColor(4);
  grame_TrigFix->SetMarkerColor(4);

  mgme->SetTitle(h_total->GetTitle());
  TCanvas *cme = new TCanvas("c","",200,10,600,500);

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
   legendme->AddEntry(grame_singlEl,"SingleEle","p");
   legendme->AddEntry(grame_singlMu,"SingleMu","p");
   legendme->AddEntry(grame_ElMu,"E+Mu","p");
   legendme->AddEntry(grame_DoubleMu,"DoubleMu","p");
   legendme->AddEntry(grame_DoubleE,"DoubleE","p");
   //legendme->AddEntry(grame_Trig,"Comb","p");
   legendme->AddEntry(grame_TrigFix,"Comb new formula","p");
   legendme->Draw();


  cme->SaveAs("ggH_TriggerEff_from"+tag+"TnP_"+var+"_me.png");

  cme->Clear();




   TH1F *hmm_total;
   TH1F *hmm_pass_singlEl;
   TH1F *hmm_pass_singlMu;
   TH1F *hmm_pass_ElMu;
   TH1F *hmm_pass_DoubleMu;
   TH1F *hmm_pass_DoubleE;
   TH1F *hmm_pass_Trig;
   TH1F *hmm_pass_TrigFix;

  // TGraphAsymmErrors *gra_2018A=0;

  hmm_total = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww");
  hmm_pass_singlEl = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_singlEl");
  hmm_pass_singlMu = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_singlMu");
  hmm_pass_ElMu = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_ElMu");
  hmm_pass_DoubleMu = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_dblMu");
  hmm_pass_DoubleE = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_dblEl");
  hmm_pass_Trig = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_Trig");
  hmm_pass_TrigFix = (TH1F*)ffix->Get("hww2l2v_13TeV_mm/"+var+"/histo_ggH_hww_Trig");


  TMultiGraph *mgmm = new TMultiGraph();
  TGraphAsymmErrors *gramm_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_Trig = new TGraphAsymmErrors();
  TGraphAsymmErrors *gramm_TrigFix = new TGraphAsymmErrors();


  gramm_singlEl = new TGraphAsymmErrors (hmm_pass_singlEl,hmm_total,"cp");
  gramm_singlMu = new TGraphAsymmErrors (hmm_pass_singlMu,hmm_total,"cp");
  gramm_ElMu = new TGraphAsymmErrors (hmm_pass_ElMu,hmm_total,"cp");
  gramm_DoubleMu = new TGraphAsymmErrors (hmm_pass_DoubleMu,hmm_total,"cp");
  gramm_DoubleE = new TGraphAsymmErrors (hmm_pass_DoubleE,hmm_total,"cp");
  //gramm_Trig = new TGraphAsymmErrors (hmm_pass_Trig,hmm_total,"cp");
  gramm_TrigFix = new TGraphAsymmErrors (hmm_pass_TrigFix,hmm_total,"cp");


  mgmm->Add(gramm_singlEl);
  mgmm->Add(gramm_singlMu);
  mgmm->Add(gramm_ElMu);
  mgmm->Add(gramm_DoubleMu);
  mgmm->Add(gramm_DoubleE);
  //mgmm->Add(gramm_Trig);
  mgmm->Add(gramm_TrigFix);

  gramm_singlEl->SetLineColor(1);
  gramm_singlMu->SetLineColor(2);
  gramm_ElMu->SetLineColor(3);
  gramm_DoubleMu->SetLineColor(5);
  gramm_DoubleE->SetLineColor(7);
  gramm_Trig->SetLineColor(4);
  gramm_TrigFix->SetLineColor(4);

  gramm_singlEl->SetMarkerStyle(20);
  gramm_singlMu->SetMarkerStyle(20);
  gramm_ElMu->SetMarkerStyle(20);
  gramm_DoubleMu->SetMarkerStyle(20);
  gramm_DoubleE->SetMarkerStyle(20);
  gramm_Trig->SetMarkerStyle(20);
  gramm_TrigFix->SetMarkerStyle(20);

  gramm_singlEl->SetMarkerColor(1);
  gramm_singlMu->SetMarkerColor(2);
  gramm_ElMu->SetMarkerColor(3);
  gramm_DoubleMu->SetMarkerColor(5);
  gramm_DoubleE->SetMarkerColor(7);
  gramm_Trig->SetMarkerColor(4);
  gramm_TrigFix->SetMarkerColor(4);

  mgmm->SetTitle(h_total->GetTitle());
  TCanvas *cmm = new TCanvas("c","",200,10,600,500);

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
   legendmm->AddEntry(gramm_singlEl,"SingleEle","p");
   legendmm->AddEntry(gramm_singlMu,"SingleMu","p");
   legendmm->AddEntry(gramm_ElMu,"E+Mu","p");
   legendmm->AddEntry(gramm_DoubleMu,"DoubleMu","p");
   legendmm->AddEntry(gramm_DoubleE,"DoubleE","p");
   //legendmm->AddEntry(gramm_Trig,"Comb","p");
   legendmm->AddEntry(gramm_TrigFix,"Comb new formula","p");
   legendmm->Draw();


  cmm->SaveAs("ggH_TriggerEff_from"+tag+"TnP_"+var+"_mm.png");

  cmm->Clear();




   TH1F *hee_total;
   TH1F *hee_pass_singlEl;
   TH1F *hee_pass_singlMu;
   TH1F *hee_pass_ElMu;
   TH1F *hee_pass_DoubleMu;
   TH1F *hee_pass_DoubleE;
   TH1F *hee_pass_Trig;
   TH1F *hee_pass_TrigFix;

  // TGraphAsymmErrors *gra_2018A=0;

  hee_total = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww");
  hee_pass_singlEl = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_singlEl");
  hee_pass_singlMu = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_singlMu");
  hee_pass_ElMu = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_ElMu");
  hee_pass_DoubleMu = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_dblMu");
  hee_pass_DoubleE = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_dblEl");
  hee_pass_Trig = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_Trig");
  hee_pass_TrigFix = (TH1F*)ffix->Get("hww2l2v_13TeV_ee/"+var+"/histo_ggH_hww_Trig");


  TMultiGraph *mgee = new TMultiGraph();
  TGraphAsymmErrors *graee_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_Trig = new TGraphAsymmErrors();
  TGraphAsymmErrors *graee_TrigFix = new TGraphAsymmErrors();


  graee_singlEl = new TGraphAsymmErrors (hee_pass_singlEl,hee_total,"cp");
  graee_singlMu = new TGraphAsymmErrors (hee_pass_singlMu,hee_total,"cp");
  graee_ElMu = new TGraphAsymmErrors (hee_pass_ElMu,hee_total,"cp");
  graee_DoubleMu = new TGraphAsymmErrors (hee_pass_DoubleMu,hee_total,"cp");
  graee_DoubleE = new TGraphAsymmErrors (hee_pass_DoubleE,hee_total,"cp");
  //graee_Trig = new TGraphAsymmErrors (hee_pass_Trig,hee_total,"cp");
  graee_TrigFix = new TGraphAsymmErrors (hee_pass_TrigFix,hee_total,"cp");


  mgee->Add(graee_singlEl);
  mgee->Add(graee_singlMu);
  mgee->Add(graee_ElMu);
  mgee->Add(graee_DoubleMu);
  mgee->Add(graee_DoubleE);
  //mgee->Add(graee_Trig);
  mgee->Add(graee_TrigFix);

  graee_singlEl->SetLineColor(1);
  graee_singlMu->SetLineColor(2);
  graee_ElMu->SetLineColor(3);
  graee_DoubleMu->SetLineColor(5);
  graee_DoubleE->SetLineColor(7);
  graee_Trig->SetLineColor(4);
  graee_TrigFix->SetLineColor(4);

  graee_singlEl->SetMarkerStyle(20);
  graee_singlMu->SetMarkerStyle(20);
  graee_ElMu->SetMarkerStyle(20);
  graee_DoubleMu->SetMarkerStyle(20);
  graee_DoubleE->SetMarkerStyle(20);
  graee_Trig->SetMarkerStyle(20);
  graee_TrigFix->SetMarkerStyle(20);

  graee_singlEl->SetMarkerColor(1);
  graee_singlMu->SetMarkerColor(2);
  graee_ElMu->SetMarkerColor(3);
  graee_DoubleMu->SetMarkerColor(5);
  graee_DoubleE->SetMarkerColor(7);
  graee_Trig->SetMarkerColor(4);
  graee_TrigFix->SetMarkerColor(4);

  mgee->SetTitle(h_total->GetTitle());
  TCanvas *cee = new TCanvas("c","",200,10,600,500);

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
   legendee->AddEntry(graee_singlEl,"SingleEle","p");
   legendee->AddEntry(graee_singlMu,"SingleMu","p");
   legendee->AddEntry(graee_ElMu,"E+Mu","p");
   legendee->AddEntry(graee_DoubleMu,"DoubleMu","p");
   legendee->AddEntry(graee_DoubleE,"DoubleE","p");
   //legendee->AddEntry(graee_Trig,"Comb","p");
   legendee->AddEntry(graee_TrigFix,"Comb new formula","p");
   legendee->Draw();


  cee->SaveAs("ggH_TriggerEff_from"+tag+"TnP_"+var+"_ee.png");

  cee->Clear();

}
