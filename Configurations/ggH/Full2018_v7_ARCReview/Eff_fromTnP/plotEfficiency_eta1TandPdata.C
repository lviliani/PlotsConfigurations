void plotEfficiency_eta1() {

TFile *f = TFile::Open("rootFile_TandP_data/plots_ggH2018_v7_TnPEff.root");

   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_em/eta1/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_em/eta1/histo_ggH_hww_singlEl");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_em/eta1/histo_ggH_hww_singlMu");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_em/eta1/histo_ggH_hww_ElMu");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_em/eta1/histo_ggH_hww_Trig");

//for(int i = 1; i < h_pass->GetNbinsX(); i ++) {
//cout << "total =  " << h_total->GetBinContent(i) << "  " << "pass = " <<  h_pass->GetBinContent(i) << endl;
//}

  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();

  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);
  gra_ElMu = new TGraphAsymmErrors (h_pass_ElMu,h_total);
  gra_Trig = new TGraphAsymmErrors (h_pass_Trig,h_total);

  mg->Add(gra_singlEl);
  mg->Add(gra_singlMu);
  mg->Add(gra_ElMu);
  mg->Add(gra_Trig);


  gra_singlEl->SetLineColor(1);
  gra_singlMu->SetLineColor(2);
  gra_ElMu->SetLineColor(3);
  gra_Trig->SetLineColor(4);

  gra_singlEl->SetMarkerStyle(20);
  gra_singlMu->SetMarkerStyle(20);
  gra_ElMu->SetMarkerStyle(20);
  gra_Trig->SetMarkerStyle(20);

  gra_singlEl->SetMarkerColor(1);
  gra_singlMu->SetMarkerColor(2);
  gra_ElMu->SetMarkerColor(3);
  gra_Trig->SetMarkerColor(4);


  mg->SetTitle(h_total->GetTitle());
  TCanvas *c = new TCanvas("c","",200,10,600,500);
  
  mg->Draw("APE");
  mg->SetMinimum(0.0);
  mg->SetMaximum(1.015);
  mg->GetXaxis()->SetTitle("eta1");
  mg->GetXaxis()->CenterTitle(1);
  mg->GetXaxis()->SetTitleOffset(1.2);
  mg->GetYaxis()->SetTitle("Trig Eff");
  mg->GetYaxis()->CenterTitle(1);
  mg->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legend = new TLegend(0.5,0.1,0.7,0.3);
   legend->AddEntry(gra_singlEl,"SingleEle","p");
   legend->AddEntry(gra_singlMu,"SingleMu","p");
   legend->AddEntry(gra_ElMu,"E+Mu","p");
   legend->AddEntry(gra_Trig,"Comb","p");
   legend->Draw();


  c->SaveAs("ggH_TriggerEff_fromMCTnP_eta1_em.png");
  c->Clear();

        delete c;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_me/eta1/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_me/eta1/histo_ggH_hww_singlEl");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_me/eta1/histo_ggH_hww_singlMu");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_me/eta1/histo_ggH_hww_ElMu");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_me/eta1/histo_ggH_hww_Trig");

//for(int i = 1; i < h_pass->GetNbinsX(); i ++) {
//cout << "total =  " << h_total->GetBinContent(i) << "  " << "pass = " <<  h_pass->GetBinContent(i) << endl;
//}

  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();

  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);
  gra_ElMu = new TGraphAsymmErrors (h_pass_ElMu,h_total);
  gra_Trig = new TGraphAsymmErrors (h_pass_Trig,h_total);

  mg->Add(gra_singlEl);
  mg->Add(gra_singlMu);
  mg->Add(gra_ElMu);
  mg->Add(gra_Trig);


  gra_singlEl->SetLineColor(1);
  gra_singlMu->SetLineColor(2);
  gra_ElMu->SetLineColor(3);
  gra_Trig->SetLineColor(4);

  gra_singlEl->SetMarkerStyle(20);
  gra_singlMu->SetMarkerStyle(20);
  gra_ElMu->SetMarkerStyle(20);
  gra_Trig->SetMarkerStyle(20);

  gra_singlEl->SetMarkerColor(1);
  gra_singlMu->SetMarkerColor(2);
  gra_ElMu->SetMarkerColor(3);
  gra_Trig->SetMarkerColor(4);


  mg->SetTitle(h_total->GetTitle());
  TCanvas *c = new TCanvas("c","",200,10,600,500);

  mg->Draw("APE");
  mg->SetMinimum(0.0);
  mg->SetMaximum(1.015);
  mg->GetXaxis()->SetTitle("eta1");
  mg->GetXaxis()->CenterTitle(1);
  mg->GetXaxis()->SetTitleOffset(1.2);
  mg->GetYaxis()->SetTitle("Trig Eff");
  mg->GetYaxis()->CenterTitle(1);
  mg->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legend = new TLegend(0.5,0.1,0.7,0.3);
   legend->AddEntry(gra_singlEl,"SingleEle","p");
   legend->AddEntry(gra_singlMu,"SingleMu","p");
   legend->AddEntry(gra_ElMu,"E+Mu","p");
   legend->AddEntry(gra_Trig,"Comb","p");
   legend->Draw();


  c->SaveAs("ggH_TriggerEff_fromMCTnP_eta1.png");
  c->Clear();

        delete c;


}// end of program
