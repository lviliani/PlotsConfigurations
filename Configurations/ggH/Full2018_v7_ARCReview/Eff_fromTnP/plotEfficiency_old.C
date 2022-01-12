void plotEfficiency(TString var="eta1", bool isData=false){ 

TString dir = isData ? "rootFile_TandP_data" : "rootFile";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7_TnPEff.root");

   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_Trig;

  // TGraphAsymmErrors *gra_2018A=0;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_singlEl");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_singlMu");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_ElMu");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_em/"+var+"/histo_ggH_hww_Trig");

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
  mg->GetXaxis()->SetTitle(""+var+"");
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

  TString tag = isData ? "DATA" : "MC";

  c->SaveAs("ggH_TriggerEff_from"+tag+"TnP_"+var+"_em.png");
  c->Clear();

        delete c;


   TH1F *hme_total;
   TH1F *hme_pass_singlEl;
   TH1F *hme_pass_singlMu;
   TH1F *hme_pass_ElMu;
   TH1F *hme_pass_Trig;


  hme_total = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww");
  hme_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_singlEl");
  hme_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_singlMu");
  hme_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_ElMu");
  hme_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_me/"+var+"/histo_ggH_hww_Trig");

//for(int i = 1; i < h_pass->GetNbinsX(); i ++) {
//cout << "total =  " << h_total->GetBinContent(i) << "  " << "pass = " <<  h_pass->GetBinContent(i) << endl;
//}

  TMultiGraph *mgme = new TMultiGraph();
  TGraphAsymmErrors *grame_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors();

  grame_singlEl = new TGraphAsymmErrors (hme_pass_singlEl,hme_total);
  grame_singlMu = new TGraphAsymmErrors (hme_pass_singlMu,hme_total);
  grame_ElMu = new TGraphAsymmErrors (hme_pass_ElMu,hme_total);
  grame_Trig = new TGraphAsymmErrors (hme_pass_Trig,hme_total);

  mgme->Add(grame_singlEl);
  mgme->Add(grame_singlMu);
  mgme->Add(grame_ElMu);
  mgme->Add(grame_Trig);


  grame_singlEl->SetLineColor(1);
  grame_singlMu->SetLineColor(2);
  grame_ElMu->SetLineColor(3);
  grame_Trig->SetLineColor(4);

  grame_singlEl->SetMarkerStyle(20);
  grame_singlMu->SetMarkerStyle(20);
  grame_ElMu->SetMarkerStyle(20);
  grame_Trig->SetMarkerStyle(20);

  grame_singlEl->SetMarkerColor(1);
  grame_singlMu->SetMarkerColor(2);
  grame_ElMu->SetMarkerColor(3);
  grame_Trig->SetMarkerColor(4);


  mgme->SetTitle(hme_total->GetTitle());
  TCanvas *cme = new TCanvas("cme","",200,10,600,500);

  mgme->Draw("APE");
  mgme->SetMinimum(0.0);
  mgme->SetMaximum(1.015);
  mgme->GetXaxis()->SetTitle(""+var+"");
  mgme->GetXaxis()->CenterTitle(1);
  mgme->GetXaxis()->SetTitleOffset(1.2);
  mgme->GetYaxis()->SetTitle("Trig Eff");
  mgme->GetYaxis()->CenterTitle(1);
  mgme->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legendme = new TLegend(0.5,0.1,0.7,0.3);
   legendme->AddEntry(gra_singlEl,"SingleEle","p");
   legendme->AddEntry(gra_singlMu,"SingleMu","p");
   legendme->AddEntry(gra_ElMu,"E+Mu","p");
   legendme->AddEntry(gra_Trig,"Comb","p");
   legendme->Draw();

  cme->SaveAs("ggH_TriggerEff_from"+tag+"TnP_"+var+"_me.png");

  cme->Clear();

        delete cme;


}// end of program
